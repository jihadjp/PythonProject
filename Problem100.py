from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT

pdfmetrics.registerFont(TTFont('Bengali', 'C:/Users/pc/Downloads/NotoSansBengali-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Bengali-Bold', 'C:/Users/pc/Downloads/NotoSansBengali-Bold.ttf'))

doc = SimpleDocTemplate('routine_67_O.pdf',
                        pagesize=A4,
                        topMargin=14*mm,
                        bottomMargin=14*mm,
                        leftMargin=12*mm,
                        rightMargin=12*mm)

W, H = A4

BLUE_DARK  = colors.HexColor('#185FA5')
BLUE_MID   = colors.HexColor('#378ADD')
BLUE_LIGHT = colors.HexColor('#E6F1FB')
GREEN_BG   = colors.HexColor('#EAF3DE')
GREEN_DK   = colors.HexColor('#27500A')
GREEN_MID  = colors.HexColor('#3B6D11')
AMBER_BG   = colors.HexColor('#FAEEDA')
AMBER_DK   = colors.HexColor('#633806')
PURPLE_BG  = colors.HexColor('#EEEDFE')
PURPLE_DK  = colors.HexColor('#3C3489')
CORAL_BG   = colors.HexColor('#FAECE7')
CORAL_DK   = colors.HexColor('#712B13')
TEAL_BG    = colors.HexColor('#1D9E75')
TEAL_LT    = colors.HexColor('#E1F5EE')
GRAY_BG    = colors.HexColor('#F1EFE8')
GRAY_DK    = colors.HexColor('#444441')
WHITE      = colors.white
BLACK      = colors.HexColor('#2C2C2A')

def P(text, font='Bengali', size=8, color=BLACK, align=TA_LEFT, leading=None):
    return Paragraph(text, ParagraphStyle(
        'x', fontName=font, fontSize=size,
        textColor=color, alignment=align,
        leading=leading or size*1.35,
        spaceAfter=0, spaceBefore=0,
    ))

def PC(text, font='Bengali', size=8, color=BLACK):
    return P(text, font, size, color, TA_CENTER)

story = []

# Title
story.append(P('ক্লাস রুটিন — 67_O', 'Bengali-Bold', 18, BLUE_DARK, TA_CENTER))
story.append(Spacer(1, 2*mm))
story.append(P('নামাজ প্রথম, তারপর সব কাজ  •  ঘুম ৬ ঘণ্টা  •  Project + পড়াশোনা', 'Bengali', 9, GRAY_DK, TA_CENTER))
story.append(Spacer(1, 3*mm))

# Namaz times box
namaz_data = [
    [PC('ফজর', 'Bengali-Bold', 8, GREEN_DK),
     PC('যোহর', 'Bengali-Bold', 8, GREEN_DK),
     PC('আসর', 'Bengali-Bold', 8, GREEN_DK),
     PC('মাগরিব', 'Bengali-Bold', 8, GREEN_DK),
     PC('এশা', 'Bengali-Bold', 8, GREEN_DK)],
    [PC('৪:৪০ AM', 'Bengali', 8, GREEN_DK),
     PC('১:৩০ PM', 'Bengali', 8, GREEN_DK),
     PC('৫:১৫ PM', 'Bengali', 8, GREEN_DK),
     PC('আজানের ৫ মিনিট পর', 'Bengali', 7, GREEN_DK),
     PC('৮:৪৫ PM', 'Bengali', 8, GREEN_DK)],
]
nt = Table(namaz_data, colWidths=[35*mm]*5)
nt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GREEN_BG),
    ('GRID', (0,0), (-1,-1), 0.5, GREEN_MID),
    ('ROUNDEDCORNERS', [4]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(nt)
story.append(Spacer(1, 3*mm))

# Legend
leg_data = [[
    PC('■ নামাজ', 'Bengali', 7.5, GREEN_DK),
    PC('■ ঘুম', 'Bengali', 7.5, colors.HexColor('#0C447C')),
    PC('■ Class/Lab', 'Bengali', 7.5, PURPLE_DK),
    PC('■ Deep Work', 'Bengali', 7.5, colors.HexColor('#085041')),
    PC('■ Project', 'Bengali', 7.5, AMBER_DK),
    PC('■ পড়াশোনা', 'Bengali', 7.5, CORAL_DK),
    PC('■ Break/খাওয়া', 'Bengali', 7.5, GRAY_DK),
]]
lt = Table(leg_data, colWidths=[25*mm, 18*mm, 22*mm, 22*mm, 18*mm, 22*mm, 28*mm])
lt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GRAY_BG),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('ROUNDEDCORNERS', [3]),
]))
story.append(lt)
story.append(Spacer(1, 4*mm))

TAG_SLEEP   = (BLUE_LIGHT, colors.HexColor('#0C447C'))
TAG_NAMAZ   = (GREEN_BG,   GREEN_DK)
TAG_CLASS   = (PURPLE_BG,  PURPLE_DK)
TAG_DW      = (TEAL_LT,    colors.HexColor('#085041'))
TAG_PROJECT = (AMBER_BG,   AMBER_DK)
TAG_STUDY   = (CORAL_BG,   CORAL_DK)
TAG_BREAK   = (GRAY_BG,    GRAY_DK)

days = [
    {
        'name': 'শনিবার (Saturday)',
        'type': 'class',
        'note': 'Class: ৮:৩০ AM থেকে',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                                      'ঘুম',    TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                                     'ফজর',    TAG_NAMAZ,   True),
            ('০৫:০০–০৭:০০', 'ঘুম (২য় শিফট)',                                          'ঘুম',    TAG_SLEEP,   False),
            ('০৭:০০–০৭:৩০', 'ঘুম / বাকি বিশ্রাম',                                    'ঘুম',    TAG_SLEEP,   False),
            ('০৭:৩০–০৮:১৫', 'নাস্তা + Varsity প্রস্তুতি',                            'বিরতি',  TAG_BREAK,   False),
            ('০৮:৩০–১০:০০', 'DBMS – CSE311 · KT-222 (MDA)',                            'Class',  TAG_CLASS,   False),
            ('১০:০০–১১:৩০', 'Campus পড়াশোনা / বিরতি',                                'বিরতি',  TAG_BREAK,   False),
            ('১১:৩০–১৩:০০', 'Numerical Methods – CSE226 · KT-222 (MMR)',               'Class',  TAG_CLASS,   False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                                    'যোহর',   TAG_NAMAZ,   True),
            ('১৩:৪৫–১৪:৩০', 'Compiler Design – CSE313 · KT-318(B) (UH)',              'Class',  TAG_CLASS,   False),
            ('১৪:৩০–১৫:০০', 'Lunch / বিশ্রাম',                                        'Lunch',  TAG_BREAK,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                                     'আসর',    TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project Development',                                     'Project',TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                                  'মাগরিব', TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project Development (চলবে)',                              'Project',TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                                     'এশা',    TAG_NAMAZ,   True),
            ('৯:০৫–২১:৩০',  'University Course পড়াশোনা + Assignment',                'Study',  TAG_STUDY,   False),
            ('২১:৩০–২২:৩০', 'Dinner + Family Time',                                    'Dinner', TAG_BREAK,   False),
            ('২২:৩০–০০:০০', 'পড়াশোনা / পরের দিনের plan',                            'Study',  TAG_STUDY,   False),
        ]
    },
    {
        'name': 'রবিবার (Sunday)',
        'type': 'class',
        'note': 'Lab: ৮:৩০ AM থেকে',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                                                          'ঘুম',    TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                                                         'ফজর',    TAG_NAMAZ,   True),
            ('০৫:০০–০৭:৩০', 'ঘুম (২য় শিফট)',                                                             'ঘুম',    TAG_SLEEP,   False),
            ('০৭:৩০–০৮:১৫', 'নাস্তা + Lab প্রস্তুতি',                                                   'বিরতি',  TAG_BREAK,   False),
            ('০৮:৩০–১১:৩০', 'DBMS Lab CSE312(O1)·G1-004 | Compiler Lab CSE314(O2)·G1-005',               'Lab',    TAG_CLASS,   False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                                                        'যোহর',   TAG_NAMAZ,   True),
            ('১৩:৪৫–১৪:৩০', 'DBMS Lab CSE312(O2)·G1-016 | Compiler Lab CSE314(O1)·G1-020',               'Lab',    TAG_CLASS,   False),
            ('১৪:৩০–১৫:০০', 'Lunch / বিশ্রাম / বাসায় ফেরা',                                           'Lunch',  TAG_BREAK,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                                                         'আসর',    TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project Development',                                                        'Project',TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                                                     'মাগরিব', TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project Development (চলবে)',                                                 'Project',TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                                                         'এশা',    TAG_NAMAZ,   True),
            ('৯:০৫–২১:৩০',  'University Course পড়াশোনা + Assignment',                                   'Study',  TAG_STUDY,   False),
            ('২১:৩০–২২:৩০', 'Dinner + Family Time',                                                       'Dinner', TAG_BREAK,   False),
            ('২২:৩০–০০:০০', 'পড়াশোনা / পরের দিনের plan',                                               'Study',  TAG_STUDY,   False),
        ]
    },
    {
        'name': 'সোমবার (Monday)',
        'type': 'off',
        'note': 'Off Day — সকাল থেকে Deep Work',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                        'ঘুম',     TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                       'ফজর',     TAG_NAMAZ,   True),
            ('০৫:০০–০৭:৩০', 'ঘুম (২য় শিফট)',                           'ঘুম',     TAG_SLEEP,   False),
            ('০৭:৩০–০৮:০০', 'নাস্তা',                                   'নাস্তা',  TAG_BREAK,   False),
            ('০৮:০০–১:৩০',  'Deep Work — Project Development (একটানা)', 'Deep Work',TAG_DW,    False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                      'যোহর',    TAG_NAMAZ,   True),
            ('১৩:৫০–১৫:০০', 'Lunch + বিশ্রাম',                          'Lunch',   TAG_BREAK,   False),
            ('১৫:০০–৫:১৫',  'Complex Topics / Difficult Chapters',       'Study',   TAG_STUDY,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                       'আসর',     TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project Development (2nd Session)',         'Project', TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                    'মাগরিব',  TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project (চলবে)',                            'Project', TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                       'এশা',     TAG_NAMAZ,   True),
            ('৯:০৫–২১:৩০',  'Assignment + Revision',                     'Study',   TAG_STUDY,   False),
            ('২১:৩০–২২:৩০', 'Dinner + Family Time',                      'Dinner',  TAG_BREAK,   False),
            ('২২:৩০–০০:০০', 'হালকা পড়া / পরের দিনের plan',            'Study',   TAG_STUDY,   False),
        ]
    },
    {
        'name': 'মঙ্গলবার (Tuesday)',
        'type': 'off',
        'note': 'Off Day — সকাল থেকে Deep Work',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                        'ঘুম',     TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                       'ফজর',     TAG_NAMAZ,   True),
            ('০৫:০০–০৭:৩০', 'ঘুম (২য় শিফট)',                           'ঘুম',     TAG_SLEEP,   False),
            ('০৭:৩০–০৮:০০', 'নাস্তা',                                   'নাস্তা',  TAG_BREAK,   False),
            ('০৮:০০–১:৩০',  'Deep Work — Project Development',           'Deep Work',TAG_DW,    False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                      'যোহর',    TAG_NAMAZ,   True),
            ('১৩:৫০–১৫:০০', 'Lunch + বিশ্রাম',                          'Lunch',   TAG_BREAK,   False),
            ('১৫:০০–৫:১৫',  'University Coursework / Lecture Review',    'Study',   TAG_STUDY,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                       'আসর',     TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project Development',                       'Project', TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                    'মাগরিব',  TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project (চলবে)',                            'Project', TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                       'এশা',     TAG_NAMAZ,   True),
            ('৯:০৫–২২:০০',  'পড়াশোনা + Assignment',                    'Study',   TAG_STUDY,   False),
            ('২২:০০–২৩:০০', 'Dinner + Family Time',                      'Dinner',  TAG_BREAK,   False),
            ('২৩:০০–০০:০০', 'হালকা পড়া / plan',                        'Study',   TAG_STUDY,   False),
        ]
    },
    {
        'name': 'বুধবার (Wednesday)',
        'type': 'class',
        'note': 'Class: দুপুর ১:০০ থেকে — সকাল Deep Work',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                                          'ঘুম',     TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                                         'ফজর',     TAG_NAMAZ,   True),
            ('০৫:০০–০৭:৩০', 'ঘুম (২য় শিফট)',                                             'ঘুম',     TAG_SLEEP,   False),
            ('০৭:৩০–০৮:০০', 'নাস্তা',                                                    'নাস্তা',  TAG_BREAK,   False),
            ('০৮:০০–১:৩০',  'Deep Work — Project / Complex Topics',                       'Deep Work',TAG_DW,    False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                                        'যোহর',    TAG_NAMAZ,   True),
            ('১৩:৫০–১৪:৩০', 'Compiler Design – CSE313 · KT-303 (UH)',                     'Class',   TAG_CLASS,   False),
            ('১৪:৩০–১৬:০০', 'Numerical Methods – CSE226 · KT-303 (MMR)',                  'Class',   TAG_CLASS,   False),
            ('৫:১৫ (বিরতি)', 'আসর নামাজ — class ফাঁকে পড়ে নিন',                        'আসর',     TAG_NAMAZ,   True),
            ('১৬:০০–১৭:৩০', 'DBMS – CSE311 · KT-303 (MDA)',                               'Class',   TAG_CLASS,   False),
            ('১৭:৩০–মাগরিব','বাসায় ফেরা',                                                'বিরতি',  TAG_BREAK,   False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                                      'মাগরিব',  TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project Development',                                        'Project', TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                                         'এশা',     TAG_NAMAZ,   True),
            ('৯:০৫–২১:৩০',  'Assignment + Revision',                                      'Study',   TAG_STUDY,   False),
            ('২১:৩০–২২:৩০', 'Dinner + Family Time',                                       'Dinner',  TAG_BREAK,   False),
            ('২২:৩০–০০:০০', 'Project / plan',                                             'Project', TAG_PROJECT, False),
        ]
    },
    {
        'name': 'বৃহস্পতিবার (Thursday)',
        'type': 'off',
        'note': 'Off Day — Weekly Review দিন',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                         'ঘুম',     TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                        'ফজর',     TAG_NAMAZ,   True),
            ('০৫:০০–০৭:৩০', 'ঘুম (২য় শিফট)',                            'ঘুম',     TAG_SLEEP,   False),
            ('০৭:৩০–০৮:০০', 'নাস্তা',                                    'নাস্তা',  TAG_BREAK,   False),
            ('০৮:০০–১:৩০',  'Deep Work — Project Development',            'Deep Work',TAG_DW,    False),
            ('১:৩০',         'যোহর নামাজ + দোয়া',                       'যোহর',    TAG_NAMAZ,   True),
            ('১৩:৫০–১৫:০০', 'Lunch + বিশ্রাম',                           'Lunch',   TAG_BREAK,   False),
            ('১৫:০০–৫:১৫',  'Weekly Review + Revision + Assignment',      'Study',   TAG_STUDY,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                        'আসর',     TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project Development',                        'Project', TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                     'মাগরিব',  TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project (চলবে)',                             'Project', TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                        'এশা',     TAG_NAMAZ,   True),
            ('৯:০৫–২২:০০',  'পড়াশোনা + Dinner + Family',                'Study',   TAG_STUDY,   False),
            ('২২:০০–০০:০০', 'পরের সপ্তাহের plan / হালকা পড়া',         'Study',   TAG_STUDY,   False),
        ]
    },
    {
        'name': 'শুক্রবার (Friday)',
        'type': 'off',
        'note': 'Off Day — জুমআর দিন',
        'rows': [
            ('১২:০০–০৪:০০', 'ঘুম (Deep Sleep)',                               'ঘুম',     TAG_SLEEP,   False),
            ('০৪:৪০',        'ফজর নামাজ + দোয়া',                               'ফজর',     TAG_NAMAZ,   True),
            ('০৫:০০–০৮:০০', 'ঘুম (২য় শিফট — একটু বেশি বিশ্রাম)',             'ঘুম',     TAG_SLEEP,   False),
            ('০৮:০০–১:৩০',  'Project Development / হালকা পড়াশোনা',           'Project', TAG_PROJECT, False),
            ('১:৩০',         'যোহর / জুমআর নামাজ + খুতবা + দোয়া',            'জুমআ',   TAG_NAMAZ,   True),
            ('১৩:৩০–১৫:০০', 'Lunch + Family Time + বিশ্রাম',                  'Lunch',   TAG_BREAK,   False),
            ('৫:১৫',         'আসর নামাজ + দোয়া',                               'আসর',     TAG_NAMAZ,   True),
            ('৫:৪০–মাগরিব', 'Project / Weekly Catch-up',                       'Project', TAG_PROJECT, False),
            ('মাগরিব+৫ মি', 'মাগরিব নামাজ + দোয়া',                           'মাগরিব',  TAG_NAMAZ,   True),
            ('৬:৫৫–৮:৪৫',   'Project (চলবে)',                                  'Project', TAG_PROJECT, False),
            ('৮:৪৫',         'এশা নামাজ + দোয়া',                               'এশা',     TAG_NAMAZ,   True),
            ('৯:০৫–২২:০০',  'Revision + Dinner + Family',                      'Study',   TAG_STUDY,   False),
            ('২২:০০–০০:০০', 'শনিবারের class প্রস্তুতি',                      'Study',   TAG_STUDY,   False),
        ]
    },
]

COL_W = [28*mm, 95*mm, 18*mm]

def tag_cell(label, bg, fg):
    return Paragraph(label, ParagraphStyle('tg',
        fontName='Bengali-Bold', fontSize=7,
        textColor=fg, alignment=TA_CENTER,
        leading=9, spaceAfter=0, spaceBefore=0))

for day in days:
    is_class = day['type'] == 'class'
    hdr_bg = BLUE_DARK if is_class else colors.HexColor('#5F5E5A')

    header = [[
        Paragraph(day['name'], ParagraphStyle('dh', fontName='Bengali-Bold', fontSize=10,
            textColor=WHITE, alignment=TA_LEFT, leading=13)),
        Paragraph(day['note'], ParagraphStyle('dn', fontName='Bengali', fontSize=8,
            textColor=colors.HexColor('#B5D4F4') if is_class else colors.HexColor('#D3D1C7'),
            alignment=TA_LEFT, leading=10)),
        Paragraph('', ParagraphStyle('e', fontName='Bengali', fontSize=8)),
    ]]
    tbl_data = []
    style_cmds = [
        ('BACKGROUND', (0,0), (-1,0), hdr_bg),
        ('SPAN', (0,0), (1,0)),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#D3D1C7')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]

    for i, (t, task, lbl, tc, is_n) in enumerate(day['rows']):
        bg_color, txt_color = tc
        row_idx = i + 1
        tbl_data.append([
            Paragraph(t, ParagraphStyle('tm', fontName='Bengali', fontSize=7.5,
                textColor=GRAY_DK, alignment=TA_CENTER, leading=10)),
            Paragraph(task, ParagraphStyle('tk', fontName='Bengali' if not is_n else 'Bengali-Bold',
                fontSize=8, textColor=GREEN_DK if is_n else BLACK, leading=11)),
            tag_cell(lbl, bg_color, txt_color),
        ])
        row_bg = GREEN_BG if is_n else (BLUE_LIGHT if 'ঘুম' in lbl else WHITE)
        style_cmds += [
            ('BACKGROUND', (0, row_idx), (-1, row_idx), row_bg),
            ('BACKGROUND', (2, row_idx), (2, row_idx), bg_color),
        ]

    full_data = header + tbl_data
    t = Table(full_data, colWidths=COL_W, repeatRows=1)
    t.setStyle(TableStyle(style_cmds))
    story.append(t)
    story.append(Spacer(1, 3*mm))

# Footer
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#D3D1C7')))
story.append(Spacer(1, 2*mm))
story.append(P('Class 67_O  •  ঘুম ৬ ঘণ্টা  •  নামাজ সর্বদা প্রথম', 'Bengali', 8, GRAY_DK, TA_CENTER))

doc.build(story)
print("PDF created successfully!")