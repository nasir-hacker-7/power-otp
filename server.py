#!/usr/bin/env python3
from flask import Flask, jsonify, render_template_string
import requests
import json

app = Flask(__name__)

API_URL = "http://51.77.216.195/crapi/dgroup/viewstats"
API_TOKEN = "RVBXRjRSQouDZnhDQZBYSWdqj2tZlWp7VnFUf3hSdVeEjXV1gGeP"

@app.route('/api/otp-data', methods=['GET'])
def get_otp_data():
    try:
        response = requests.get(f"{API_URL}?token={API_TOKEN}", timeout=10)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DANGER POWER OTP</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            padding: 20px;
            color: #fff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            animation: slideDown 0.6s ease-out;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header h1 {
            font-size: 3.5em;
            font-weight: 900;
            background: linear-gradient(45deg, #ff0000, #ff6b00, #ff0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 30px rgba(255, 0, 0, 0.5);
            margin-bottom: 10px;
            letter-spacing: 2px;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% {
                filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.5));
            }
            50% {
                filter: drop-shadow(0 0 20px rgba(255, 0, 0, 0.8));
            }
        }

        .header p {
            font-size: 1.1em;
            color: #00d4ff;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        .status-bar {
            display: flex;
            justify-content: space-around;
            align-items: center;
            background: rgba(255, 0, 0, 0.1);
            border: 2px solid #ff0000;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }

        .status-item {
            text-align: center;
        }

        .status-item .label {
            font-size: 0.9em;
            color: #00d4ff;
            margin-bottom: 5px;
        }

        .status-item .value {
            font-size: 1.8em;
            font-weight: bold;
            color: #ff0000;
        }

        .refresh-info {
            text-align: center;
            margin-bottom: 20px;
            font-size: 0.95em;
            color: #00d4ff;
        }

        .refresh-info .timer {
            font-weight: bold;
            color: #ff0000;
            font-size: 1.2em;
        }

        .otp-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            max-height: 800px;
            overflow-y: auto;
            padding-right: 10px;
        }

        .otp-container::-webkit-scrollbar {
            width: 8px;
        }

        .otp-container::-webkit-scrollbar-track {
            background: rgba(255, 0, 0, 0.1);
            border-radius: 10px;
        }

        .otp-container::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #ff0000, #ff6b00);
            border-radius: 10px;
        }

        .otp-card {
            background: linear-gradient(135deg, rgba(255, 0, 0, 0.1) 0%, rgba(255, 107, 0, 0.1) 100%);
            border: 2px solid #ff0000;
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            animation: slideIn 0.5s ease-out;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .otp-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 30px rgba(255, 0, 0, 0.6);
            border-color: #ff6b00;
        }

        .otp-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid rgba(255, 0, 0, 0.3);
        }

        .otp-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #00d4ff;
        }

        .otp-time {
            font-size: 0.85em;
            color: #ff6b00;
        }

        .otp-content {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .otp-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .otp-row:last-child {
            border-bottom: none;
        }

        .otp-label {
            font-weight: 600;
            color: #00d4ff;
            min-width: 100px;
        }

        .otp-value {
            color: #fff;
            word-break: break-all;
            text-align: right;
            flex: 1;
            margin-left: 10px;
        }

        .otp-code {
            background: linear-gradient(45deg, #ff0000, #ff6b00);
            padding: 12px 15px;
            border-radius: 8px;
            font-size: 1.4em;
            font-weight: bold;
            text-align: center;
            letter-spacing: 2px;
            margin-top: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
            user-select: none;
        }

        .otp-code:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(255, 0, 0, 0.8);
        }

        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #00d4ff;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #00d4ff;
        }

        .spinner {
            border: 4px solid rgba(255, 0, 0, 0.2);
            border-top: 4px solid #ff0000;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid rgba(255, 0, 0, 0.3);
            color: #00d4ff;
            font-size: 0.9em;
        }

        .copy-notification {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(45deg, #ff0000, #ff6b00);
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
            animation: slideInRight 0.3s ease-out;
            z-index: 1000;
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(100px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5em;
            }

            .otp-container {
                grid-template-columns: 1fr;
                max-height: 600px;
            }

            .status-bar {
                flex-direction: column;
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚡ DANGER POWER OTP ⚡</h1>
            <p>Real-Time OTP Monitoring System</p>
        </div>

        <div class="status-bar">
            <div class="status-item">
                <div class="label">📊 Total OTPs</div>
                <div class="value" id="totalOtps">0</div>
            </div>
            <div class="status-item">
                <div class="label">🔄 Auto Refresh</div>
                <div class="value" id="refreshStatus">15s</div>
            </div>
            <div class="status-item">
                <div class="label">⏱️ Next Update</div>
                <div class="value timer" id="countdown">15s</div>
            </div>
        </div>

        <div class="refresh-info">
            Status: <span style="color: #00ff00;">● LIVE</span> | Last Updated: <span id="lastUpdate">Never</span>
        </div>

        <div class="otp-container" id="otpContainer">
            <div class="loading">
                <div class="spinner"></div>
                <p>Loading OTP data...</p>
            </div>
        </div>

        <div class="footer">
            <p>Website Developer © powermodz</p>
            <p style="margin-top: 10px; font-size: 0.85em; color: #ff6b00;">DANGER POWER OTP Dashboard v1.0</p>
        </div>
    </div>

    <script>
        const API_ENDPOINT = "/api/otp-data";
        const REFRESH_INTERVAL = 15000; // 15 seconds
        
        let otpList = [];
        let countdownInterval;
        let refreshInterval;
        let countdownValue = 15;

        // Country codes mapping
        const countryMap = {
            '1': '🇺🇸 USA',
            '44': '🇬🇧 UK',
            '91': '🇮🇳 India',
            '92': '🇵🇰 Pakistan',
            '880': '🇧🇩 Bangladesh',
            '584': '🇻🇪 Venezuela',
            '55': '🇧🇷 Brazil',
            '86': '🇨🇳 China',
            '81': '🇯🇵 Japan',
            '33': '🇫🇷 France',
            '49': '🇩🇪 Germany',
            '39': '🇮🇹 Italy',
            '34': '🇪🇸 Spain',
            '61': '🇦🇺 Australia',
        };

        function getCountryInfo(number) {
            if (!number) return '🌍 Unknown';
            
            for (let code in countryMap) {
                if (number.startsWith(code)) {
                    return countryMap[code];
                }
            }
            return '🌍 International';
        }

        async function fetchOTPData() {
            try {
                const response = await fetch(API_ENDPOINT);
                const data = await response.json();

                if (data.status === 'success' && data.data) {
                    otpList = data.data;
                    renderOTPs();
                    updateLastUpdate();
                    document.getElementById('totalOtps').textContent = data.total || otpList.length;
                } else {
                    showError('Failed to fetch OTP data: ' + (data.msg || 'Unknown error'));
                }
            } catch (error) {
                console.error('Error fetching OTP data:', error);
                showError('Error connecting to API');
            }
        }

        function renderOTPs() {
            const container = document.getElementById('otpContainer');
            
            if (otpList.length === 0) {
                container.innerHTML = `
                    <div class="empty-state" style="grid-column: 1/-1;">
                        <p style="font-size: 1.2em;">📭 No OTP data available</p>
                        <p style="margin-top: 10px; opacity: 0.7;">Waiting for incoming OTPs...</p>
                    </div>
                `;
                return;
            }

            container.innerHTML = otpList.map((otp, index) => {
                const countryInfo = getCountryInfo(otp.num);
                const service = otp.cli || otp.service || 'Unknown';
                const otpCode = extractOTP(otp.message);
                
                return `
                    <div class="otp-card">
                        <div class="otp-header">
                            <div class="otp-title">✨ OTP RECEIVED BY POWER MODZ ✨</div>
                            <div class="otp-time">🕒 ${otp.dt}</div>
                        </div>
                        <div class="otp-content">
                            <div class="otp-row">
                                <span class="otp-label">📞 Number:</span>
                                <span class="otp-value">${otp.num}</span>
                            </div>
                            <div class="otp-row">
                                <span class="otp-label">🌍 Country:</span>
                                <span class="otp-value">${countryInfo}</span>
                            </div>
                            <div class="otp-row">
                                <span class="otp-label">🛠️ Service:</span>
                                <span class="otp-value">${service}</span>
                            </div>
                            <div class="otp-code" onclick="copyToClipboard('${otpCode}')">
                                ${otpCode}
                            </div>
                            <div class="otp-row">
                                <span class="otp-label">📝 Message:</span>
                                <span class="otp-value">${otp.message.substring(0, 100)}${otp.message.length > 100 ? '...' : ''}</span>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function extractOTP(message) {
            // Extract OTP code from message (usually 6 digit numbers)
            // First try to find 6-digit OTP
            let match = message.match(/(\d{6})/);
            if (match) return match[1];
            
            // If not found, try 5-digit
            match = message.match(/(\d{5})/);
            if (match) return match[1];
            
            // If not found, try 4-digit
            match = message.match(/(\d{4})/);
            if (match) return match[1];
            
            // Fallback to any digits
            match = message.match(/(\d{3,})/);
            return match ? match[1] : 'N/A';
        }

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                showNotification(`OTP Copied: ${text}`);
            }).catch(err => {
                console.error('Failed to copy:', err);
            });
        }

        function showNotification(message) {
            const notification = document.createElement('div');
            notification.className = 'copy-notification';
            notification.textContent = message;
            document.body.appendChild(notification);

            setTimeout(() => {
                notification.remove();
            }, 3000);
        }

        function showError(message) {
            const container = document.getElementById('otpContainer');
            container.innerHTML = `
                <div class="empty-state" style="grid-column: 1/-1;">
                    <p style="color: #ff0000; font-size: 1.2em;">❌ ${message}</p>
                </div>
            `;
        }

        function updateLastUpdate() {
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            document.getElementById('lastUpdate').textContent = timeString;
        }

        function startCountdown() {
            countdownValue = 15;
            
            if (countdownInterval) clearInterval(countdownInterval);
            
            countdownInterval = setInterval(() => {
                countdownValue--;
                document.getElementById('countdown').textContent = countdownValue + 's';
                
                if (countdownValue <= 0) {
                    clearInterval(countdownInterval);
                    fetchOTPData();
                    startCountdown();
                }
            }, 1000);
        }

        // Initial load
        fetchOTPData();
        startCountdown();

        // Refresh every 15 seconds
        refreshInterval = setInterval(() => {
            fetchOTPData();
            startCountdown();
        }, REFRESH_INTERVAL);

        // Cleanup on page unload
        window.addEventListener('beforeunload', () => {
            if (countdownInterval) clearInterval(countdownInterval);
            if (refreshInterval) clearInterval(refreshInterval);
        });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
