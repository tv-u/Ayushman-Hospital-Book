import os

# 1. यदि प्रोजेक्ट में app.py या main.py (Flask/FastAPI) है, तो उसे आधुनिक फ्रंटएंड के साथ अपडेट करें
html_code = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayushman Hospital Finder & Portal</title>
    <!-- Tailwind CSS for Responsive Design & Smooth UI -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
        .smooth-transition { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 flex flex-col min-h-screen">

    <!-- Premium Navigation -->
    <header class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="bg-indigo-600 text-white p-2 rounded-xl font-bold text-lg shadow-md">🏥</div>
                <span class="text-xl font-bold bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">Ayushman Portal</span>
            </div>
            <nav class="hidden md:flex items-center space-x-6 text-sm font-medium text-slate-600">
                <a href="#" class="hover:text-indigo-600 smooth-transition">होम</a>
                <a href="#" class="hover:text-indigo-600 smooth-transition">अस्पताल खोजें</a>
                <a href="#" class="hover:text-indigo-600 smooth-transition">सिंक स्टेटस</a>
                <a href="#" class="hover:text-indigo-600 smooth-transition">सहायता</a>
            </nav>
            <div>
                <button class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-xl text-sm font-medium shadow-md shadow-indigo-200 smooth-transition">डेटा सिंक करें</button>
            </div>
        </div>
    </header>

    <!-- Main Content Area with Responsive Layout & Smooth Animations -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
        <div class="text-center py-12">
            <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mb-4 animate-fade-in">आयुष्मान भारत अस्पताल डेटा पोर्टल</h1>
            <p class="text-slate-600 max-w-2xl mx-auto text-base sm:text-lg mb-8">मोबाइल और डेस्कटॉप दोनों के लिए पूरी तरह से ऑप्टिमाइज़्ड और ऑटो-सिंक होने वाला आधुनिक प्लेटफॉर्म।</p>
            
            <!-- Quick Stats / Cards Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md smooth-transition">
                    <div class="text-indigo-600 text-2xl font-bold mb-2">🔄</div>
                    <h3 class="text-lg font-semibold text-slate-900">ऑटो-सिंक स्टेटस</h3>
                    <p class="text-slate-500 text-sm mt-1">डेटा.gov.in से प्रतिदिन ऑटो-अपडेट सक्रिय।</p>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md smooth-transition">
                    <div class="text-emerald-600 text-2xl font-bold mb-2">⚡</div>
                    <h3 class="text-lg font-semibold text-slate-900">फास्ट रिस्पॉन्स</h3>
                    <p class="text-slate-500 text-sm mt-1">मोबाइल और डेस्कटॉप पर सुपर-फास्ट परफॉर्मेंस।</p>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md smooth-transition sm:col-span-2 lg:col-span-1">
                    <div class="text-blue-600 text-2xl font-bold mb-2">🛡️</div>
                    <h3 class="text-lg font-semibold text-slate-900">सुरक्षित डेटाबेस</h3>
                    <p class="text-slate-500 text-sm mt-1">लोकल SQLite डेटाबेस सुरक्षित रूप से प्रबंधित।</p>
                </div>
            </div>
        </div>
    </main>

    <!-- Professional Footer -->
    <footer class="bg-slate-900 text-slate-400 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="space-y-4">
                <div class="flex items-center space-x-3">
                    <div class="bg-indigo-600 text-white p-2 rounded-xl font-bold text-base">🏥</div>
                    <span class="text-white font-bold text-lg">Ayushman Portal</span>
                </div>
                <p class="text-sm text-slate-400">सरकारी डेटा के साथ ऑटो-सिंक होने वाला आधुनिक और रिस्पॉन्सिव अस्पताल निर्देशिका।</p>
            </div>
            <div>
                <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">त्वरित लिंक</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="#" class="hover:text-white smooth-transition">होमपेज</a></li>
                    <li><a href="#" class="hover:text-white smooth-transition">अस्पताल सूची</a></li>
                    <li><a href="#" class="hover:text-white smooth-transition">सिंक सेटिंग्स</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">तकनीकी सहायता</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="#" class="hover:text-white smooth-transition">Termux निर्देश</a></li>
                    <li><a href="#" class="hover:text-white smooth-transition">API इंटीग्रेशन</a></li>
                    <li><a href="#" class="hover:text-white smooth-transition">एरर फिक्स गाइड</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">अपडेट्स</h4>
                <p class="text-sm text-slate-400 mb-3">दैनिक ऑटो-सिंक और नए फीचर्स की जानकारी सीधे प्राप्त करें।</p>
                <div class="flex">
                    <input type="email" placeholder="अपनी ईमेल दर्ज करें" class="bg-slate-800 border border-slate-700 px-3 py-2 rounded-l-xl text-sm text-white focus:outline-none focus:border-indigo-500 w-full">
                    <button class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-r-xl text-sm font-medium smooth-transition">जॉइन</label>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 border-t border-slate-800 text-center text-xs text-slate-500">
            &copy; 2026 Ayushman Hospital Portal. सभी अधिकार सुरक्षित।
        </div>
    </footer>

</body>
</html>
"""

# templates फ़ोल्डर सुनिश्चित करें और index.html सेव करें
os.makedirs('templates', exist_ok=True)
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("✅ Responsive UI, Smooth Animations, Premium Navigation, और Professional Footer सफलता पूर्वक सेट हो गए हैं!")
