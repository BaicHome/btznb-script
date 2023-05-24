import os
import shutil
import zipfile
import argparse
import subprocess

# 定义函数检查并安装依赖项
def check_install(package):
    try:
        importlib.import_module(package)
    except ImportError as e:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# 定义函数打印带颜色的信息
def print_color(text, color):
    if color == "red":
        print("\033[91m{}\033[00m".format(text))
    elif color == "green":
        print("\033[92m{}\033[00m".format(text))
    elif color == "yellow":
        print("\033[93m{}\033[00m".format(text))

# 检查是否以root权限运行程序
if not os.geteuid() == 0:
    print_color("Please run this program as root", "red")
    exit()

# 定义输入参数
parser = argparse.ArgumentParser(description="自动备份网站")
parser.add_argument("-y", "--domain", required=True, type=str, help="网站主域名（不带协议头）")
parser.add_argument("-d", "--dbname", required=True, type=str, help="数据库名")
args = parser.parse_args()

# 安装缺少的依赖项
check_install("zipfile")
check_install("argparse")

# 创建备份目录
backup_dir = "/backup"
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

domain = args.domain
dbname = args.dbname

# 安装zip和unzip工具
if not shutil.which("zip") or not shutil.which("unzip"):
    if shutil.which("yum"):  # CentOS系统
        subprocess.check_call(["yum", "-y", "install", "zip", "unzip"])
    elif shutil.which("apt"):  # Ubuntu, Debian系统
        subprocess.check_call(["apt", "-y", "install", "zip", "unzip"])
    else:
        print_color("Unknown platform, unable to install zip and unzip", "red")
        exit()

print_color("欢迎使用小白-宝塔面板单站点备份工具!", "green")

# 创建临时备份目录
temp_dir = os.path.join(backup_dir, "temp")
if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

nginx_dir = os.path.join(temp_dir, "nginx")
ssl_dir = os.path.join(temp_dir, "ssl")
rewrite_dir = os.path.join(temp_dir, "rewrite")
www_dir = os.path.join(temp_dir, "www")

os.mkdir(nginx_dir)
os.mkdir(ssl_dir)
os.mkdir(rewrite_dir)
os.mkdir(www_dir)

# 备份站点文件
subprocess.check_call(["zip", "-r", os.path.join(www_dir, "www.zip"), f"/www/wwwroot/{domain}"])

# 备份nginx配置文件
shutil.copy(f"/www/server/panel/vhost/nginx/{domain}.conf", nginx_dir)

# 备份伪静态配置文件
shutil.copy(f"/www/server/panel/vhost/rewrite/{domain}.conf", rewrite_dir)

# 备份SSL证书文件
subprocess.check_call(["zip", "-r", os.path.join(ssl_dir, f"{domain}.zip"), f"/www/server/panel/vhost/cert/{domain}"])

# 备份数据库
with open("/etc/my.cnf", "r") as f:
    content = f.read()
if "skip-grant-tables" not in content:
    with open("/etc/my.cnf", "a") as f:
        f.write("\nskip-grant-tables")
    subprocess.check_call(["service", "mysql", "restart"])

subprocess.check_call(["mysqldump", "-hlocalhost", "-uroot", "-p123456", "-d", dbname, f"> {os.path.join(temp_dir, 'beifen.sql')}"])

# 打包备份文件
shutil.move(temp_dir, os.path.join(backup_dir, domain))
shutil.make_archive(os.path.join(backup_dir, domain, "beifen"), "zip", root_dir=os.path.join(backup_dir, domain))

# 清理临时文件
shutil.rmtree(os.path.join(backup_dir, domain, "temp"))

# 恢复数据库权限
with open("/etc/my.cnf", "r") as f:
    content = f.read()
if "skip-grant-tables" in content:
    content = content.replace("\nskip-grant-tables", "")
    with open("/etc/my.cnf", "w") as f:
        f.write(content)
    subprocess.check_call(["service", "mysql", "restart"])

print("==================================================================")
print_color("备份完成，如有不懂，请联系QQ：3122683591", "yellow")
print(f"备份文件保存在: {os.path.join(backup_dir, domain, 'beifen.zip')}")
print("==================================================================")
