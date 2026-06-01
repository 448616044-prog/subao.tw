#!/bin/bash
# subaotw.cn 部署脚本
# 用法: bash deploy-subaotw-cn.sh

SSH_KEY="/Users/mac/WorkBuddy/Claw/videotv-correct-ssh-key.txt"
SERVER="ubuntu@175.178.184.141"
SITE_DIR="/var/www/subaotw-cn"
LOCAL_DIR="/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn"

echo "🚀 部署 subaotw.cn..."

# 1. 创建服务器目录
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no "$SERVER" "sudo mkdir -p $SITE_DIR && sudo chown ubuntu:ubuntu $SITE_DIR"

# 2. 打包本地文件
cd "$LOCAL_DIR"
tar -czf /tmp/subaotw-cn.tar.gz --exclude='.git' --exclude='SITE-PLAN*' --exclude='*.md' .

# 3. 上传
scp -i "$SSH_KEY" -o StrictHostKeyChecking=no /tmp/subaotw-cn.tar.gz "$SERVER:/tmp/"

# 4. 解压
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no "$SERVER" "sudo tar -xzf /tmp/subaotw-cn.tar.gz -C $SITE_DIR && sudo rm /tmp/subaotw-cn.tar.gz"

# 5. 设置 nginx（如果还没设置）
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no "$SERVER" "sudo tee /etc/nginx/sites-available/subaotw-cn << 'NGINX'
server {
    listen 80;
    server_name subaotw.cn www.subaotw.cn;
    root $SITE_DIR;
    index index.html;
    location / {
        try_files \$uri \$uri/ \$uri.html =404;
    }
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf|eot)$ {
        expires 30d;
        add_header Cache-Control 'public, immutable';
    }
}
NGINX
sudo ln -sf /etc/nginx/sites-available/subaotw-cn /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx"

echo ""
echo "✅ 部署完成！"
echo "⚠️ 请确保 subaotw.cn DNS A 记录指向 175.178.184.141"
echo ""
echo "验证: curl -H 'Host: subaotw.cn' http://175.178.184.141/"
