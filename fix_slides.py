import re

html_file = '/Users/alikbekmukanbetov/Desktop/presentation/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the data for the right column for each slide
slides_to_fix = {
    4: {
        'img': 'https://page.gensparksite.com/slides_images/bffaffae3c7be7e35f667806cb9cd010.webp',
        'caption': 'Народная память',
        'sub': 'Образ батыра'
    },
    8: {
        'img': 'https://page.gensparksite.com/slides_images/a580543b8af758a308cedf06b59deec6.webp',
        'caption': 'Защита рубежей',
        'sub': 'Противостояние Коканду'
    },
    10: {
        'img': 'https://page.gensparksite.com/slides_images/6875a5bb75fd74399bedb3d8d3556df5.webp',
        'caption': 'Дипломатическая миссия',
        'sub': 'Посольство в Санкт-Петербург'
    },
    11: {
        'img': 'https://page.gensparksite.com/slides_images/1aec2657c56fb69e6889fa64095044c5.webp',
        'caption': 'Признание и Уважение',
        'sub': 'Союз с Империей'
    },
    13: {
        'img': 'https://images.unsplash.com/photo-1548685934-1422ab88c9ae?q=80&w=800',
        'caption': 'Новые горизонты',
        'sub': 'Караванная торговля'
    },
    14: {
        'img': 'https://page.gensparksite.com/slides_images/6d907892e3cc0f8e4c630aa2778905cc.webp',
        'caption': 'Северный берег Иссык-Куля',
        'sub': 'Новая родина'
    },
    16: {
        'img': 'https://page.gensparksite.com/slides_images/6875a5bb75fd74399bedb3d8d3556df5.webp',
        'caption': 'Наследие предков',
        'sub': 'Продолжение рода'
    },
    17: {
        'img': 'https://page.gensparksite.com/slides_images/a91b2917e0608ac6dc828bf5f5ebb8a4.webp',
        'caption': 'Фундамент будущего',
        'sub': 'Объединение народа'
    }
}

for slide_id, data in slides_to_fix.items():
    # Find the slide section
    pattern = r'(<div class="slide"\s*id="slide' + str(slide_id) + r'".*?<div class="flex flex-1 gap-12 items-start h-full">\s*<div class="flex-1 pr-4 h-full flex flex-col justify-center">\s*<div class="bg-white bg-opacity-70 p-8 rounded-lg shadow-sm border border-\[#e5e5e5\] backdrop-blur-sm">.*?</p>\s*</div>\s*</div>)(\s*)(</div>\s*</div>\s*</div>)'
    
    def repl(m):
        right_column = f"""
                    <div class="w-[420px] relative flex flex-col items-center justify-center h-full pb-8">
                        <div class="relative p-2 border-4 border-[#4a0404] bg-[#c5a059] shadow-2xl rounded-sm transform rotate-1 hover:rotate-0 transition-transform duration-500">
                            <div class="relative overflow-hidden h-[500px] w-full bg-gray-200">
                                <img alt="{data['caption']}" class="object-cover w-full h-full sepia-[.15] contrast-105" src="{data['img']}" />
                            </div>
                            <div class="absolute top-0 left-0 w-8 h-8 border-t-4 border-l-4 border-[#fcfbf7]"></div>
                            <div class="absolute top-0 right-0 w-8 h-8 border-t-4 border-r-4 border-[#fcfbf7]"></div>
                            <div class="absolute bottom-0 left-0 w-8 h-8 border-b-4 border-l-4 border-[#fcfbf7]"></div>
                            <div class="absolute bottom-0 right-0 w-8 h-8 border-b-4 border-r-4 border-[#fcfbf7]"></div>
                        </div>
                        <div class="mt-6 text-center w-full">
                            <div class="h-px bg-[#c5a059] w-24 mx-auto mb-2"></div>
                            <p class="text-sm font-['PT_Serif'] text-[#4a0404] italic">
                                {data['caption']}<br />({data['sub']})
                            </p>
                        </div>
                    </div>"""
        
        # Check if right column seems to be there already
        if "w-[420px]" in m.group(1):
            return m.group(0)
            
        return m.group(1) + right_column + m.group(2) + m.group(3)
        
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished fixing slides.")
