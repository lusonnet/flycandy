#!/usr/bin/env python3
"""
小鸟飞行游戏启动器
送给男朋友的小游戏
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def main():
    # 设置端口
    PORT = 8888
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 创建HTTP服务器
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 游戏服务器已启动！")
            print(f"📍 服务器地址: http://localhost:{PORT}/game.html")
            print(f"💡 按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            webbrowser.open(f'http://localhost:{PORT}/game.html')
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 游戏服务器已停止")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口")
        else:
            print(f"❌ 启动服务器时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()