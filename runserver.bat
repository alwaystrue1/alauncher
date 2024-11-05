@echo off
taskkill /f /im node.exe
taskkill /f /im python.exe
zrok disable
start python server.py
cd uv
cd Interstellar
start npm start
start npx tmole 8080
zrok enable f0himjyn8PR4
start zrok share public 4000