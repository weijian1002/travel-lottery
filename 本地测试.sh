#!/bin/bash

echo "===================================="
echo "   旅游抽签工具 - 本地测试服务器"
echo "===================================="
echo

# 检查Python是否安装
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "[错误] 未检测到Python，请先安装Python"
    echo
    echo "您也可以直接用浏览器打开 index.html 文件测试"
    exit 1
fi

echo "[提示] 服务器启动中，请稍候..."
echo
echo "===================================="
echo "   服务器信息"
echo "===================================="
echo "  访问地址: http://localhost:8080"
echo "  按 Ctrl+C 可停止服务器"
echo "===================================="
echo

# 自动打开浏览器
sleep 2
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:8080
elif command -v open &> /dev/null; then
    open http://localhost:8080
fi

# 启动Python HTTP服务器
if command -v python3 &> /dev/null; then
    python3 -m http.server 8080
else
    python -m http.server 8080
fi
