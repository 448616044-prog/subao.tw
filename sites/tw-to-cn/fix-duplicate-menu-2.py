#!/usr/bin/env python3
"""Remove duplicate mobile menu handlers from customs-guide and volume-calculator"""
import re

files = ['customs-guide.html', 'volume-calculator.html']

# Pattern matches:
# // Mobile menu
# var menuToggle = document.getElementById('menuToggle');
# var mobileMenu = document.getElementById('mobileMenu');
# if(menuToggle && mobileMenu){
#   menuToggle.addEventListener('click', function(){
#     mobileMenu.classList.toggle('active');document.body.classList.toggle("menu-open");
#     var icon = menuToggle.querySelector('i');
#     icon.classList.toggle('fa-bars');
#     icon.classList.toggle('fa-times');
#   });
#   mobileMenu.querySelectorAll('.mobile-nav-link').forEach(function(link){
#     link.addEventListener('click',function(){mobileMenu.classList.remove('active');menuToggle.querySelector('i').classList.remove('fa-times');menuToggle.querySelector('i').classList.add('fa-bars')});
#   });
# }

PATTERN = re.compile(
    r'\n\s*//\s*Mobile menu\n'
    r'\s*var\s+menuToggle\s*=\s*document\.getElementById\([^)]+\);\s*\n'
    r'\s*var\s+mobileMenu\s*=\s*document\.getElementById\([^)]+\);\s*\n'
    r'\s*if\(menuToggle\s*&&\s*mobileMenu\)\{[^}]*?menuToggle\.addEventListener\([^}]+?\}\);\s*'
    r'mobileMenu\.querySelectorAll\([^)]+\)\.forEach\([^}]+?\}\);\s*'
    r'\s*\}'
)

for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    new = PATTERN.sub('', content)
    if new != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'Fixed: {fp}')
    else:
        print(f'No match: {fp}')
