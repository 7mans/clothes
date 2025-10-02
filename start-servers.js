#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

console.log('🚀 启动 AI2Cloth 开发环境...\n');

// 启动模拟 API 服务器
console.log('📡 启动模拟 API 服务器 (端口 8010)...');
const mockServer = spawn('node', ['frontend/src/mock-server.js'], {
  stdio: 'inherit',
  cwd: process.cwd()
});

// 等待一秒让模拟服务器启动
setTimeout(() => {
  console.log('🌐 启动前端开发服务器...');
  const frontendServer = spawn('npm', ['run', 'serve'], {
    stdio: 'inherit',
    cwd: path.join(process.cwd(), 'frontend'),
    shell: true
  });

  // 处理进程退出
  process.on('SIGINT', () => {
    console.log('\n🛑 正在关闭服务器...');
    mockServer.kill();
    frontendServer.kill();
    process.exit(0);
  });

  mockServer.on('exit', (code) => {
    console.log(`模拟服务器退出，代码: ${code}`);
  });

  frontendServer.on('exit', (code) => {
    console.log(`前端服务器退出，代码: ${code}`);
  });

}, 1000);



