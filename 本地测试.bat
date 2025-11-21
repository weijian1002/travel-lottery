@echo off
chcp 65001 >nul
echo ====================================
echo    旅游抽签工具 - 本地测试服务器
echo ====================================
echo.
echo 正在启动本地服务器...
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python
    echo.
    echo 您也可以直接双击 index.html 文件在浏览器中打开测试
    pause
    exit /b 1
)

echo [提示] 服务器启动中，请稍候...
echo.
echo ====================================
echo    服务器信息
echo ====================================
echo  访问地址: http://localhost:8080
echo  按 Ctrl+C 可停止服务器
echo ====================================
echo.

REM 自动打开浏览器
timeout /t 2 /nobreak >nul
start http://localhost:8080

REM 启动Python HTTP服务器
python -m http.server 8080
