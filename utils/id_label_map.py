import sys


def get_id2label_map(dataset):
    label2id_map = get_label2id_map(dataset)

    return {val: key for key, val in label2id_map.items()}


def get_label2id_map(dataset):
    """
    Args:
        dataset: str. dataset name.
    """

    if dataset == 'kinetics400':
        label2id_map = {
            'abseiling': 0,
            'air drumming': 1,
            'answering questions': 2,
            'applauding': 3,
            'applying cream': 4,
            'archery': 5,
            'arm wrestling': 6,
            'arranging flowers': 7,
            'assembling computer': 8,
            'auctioning': 9,
            'baby waking up': 10,
            'baking cookies': 11,
            'balloon blowing': 12,
            'bandaging': 13,
            'barbequing': 14,
            'bartending': 15,
            'beatboxing': 16,
            'bee keeping': 17,
            'belly dancing': 18,
            'bench pressing': 19,
            'bending back': 20,
            'bending metal': 21,
            'biking through snow': 22,
            'blasting sand': 23,
            'blowing glass': 24,
            'blowing leaves': 25,
            'blowing nose': 26,
            'blowing out candles': 27,
            'bobsledding': 28,
            'bookbinding': 29,
            'bouncing on trampoline': 30,
            'bowling': 31,
            'braiding hair': 32,
            'breading or breadcrumbing': 33,
            'breakdancing': 34,
            'brush painting': 35,
            'brushing hair': 36,
            'brushing teeth': 37,
            'building cabinet': 38,
            'building shed': 39,
            'bungee jumping': 40,
            'busking': 41,
            'canoeing or kayaking': 42,
            'capoeira': 43,
            'carrying baby': 44,
            'cartwheeling': 45,
            'carving pumpkin': 46,
            'catching fish': 47,
            'catching or throwing baseball': 48,
            'catching or throwing frisbee': 49,
            'catching or throwing softball': 50,
            'celebrating': 51,
            'changing oil': 52,
            'changing wheel': 53,
            'checking tires': 54,
            'cheerleading': 55,
            'chopping wood': 56,
            'clapping': 57,
            'clay pottery making': 58,
            'clean and jerk': 59,
            'cleaning floor': 60,
            'cleaning gutters': 61,
            'cleaning pool': 62,
            'cleaning shoes': 63,
            'cleaning toilet': 64,
            'cleaning windows': 65,
            'climbing a rope': 66,
            'climbing ladder': 67,
            'climbing tree': 68,
            'contact juggling': 69,
            'cooking chicken': 70,
            'cooking egg': 71,
            'cooking on campfire': 72,
            'cooking sausages': 73,
            'counting money': 74,
            'country line dancing': 75,
            'cracking neck': 76,
            'crawling baby': 77,
            'crossing river': 78,
            'crying': 79,
            'curling hair': 80,
            'cutting nails': 81,
            'cutting pineapple': 82,
            'cutting watermelon': 83,
            'dancing ballet': 84,
            'dancing charleston': 85,
            'dancing gangnam style': 86,
            'dancing macarena': 87,
            'deadlifting': 88,
            'decorating the christmas tree': 89,
            'digging': 90,
            'dining': 91,
            'disc golfing': 92,
            'diving cliff': 93,
            'dodgeball': 94,
            'doing aerobics': 95,
            'doing laundry': 96,
            'doing nails': 97,
            'drawing': 98,
            'dribbling basketball': 99,
            'drinking': 100,
            'drinking beer': 101,
            'drinking shots': 102,
            'driving car': 103,
            'driving tractor': 104,
            'drop kicking': 105,
            'drumming fingers': 106,
            'dunking basketball': 107,
            'dying hair': 108,
            'eating burger': 109,
            'eating cake': 110,
            'eating carrots': 111,
            'eating chips': 112,
            'eating doughnuts': 113,
            'eating hotdog': 114,
            'eating ice cream': 115,
            'eating spaghetti': 116,
            'eating watermelon': 117,
            'egg hunting': 118,
            'exercising arm': 119,
            'exercising with an exercise ball': 120,
            'extinguishing fire': 121,
            'faceplanting': 122,
            'feeding birds': 123,
            'feeding fish': 124,
            'feeding goats': 125,
            'filling eyebrows': 126,
            'finger snapping': 127,
            'fixing hair': 128,
            'flipping pancake': 129,
            'flying kite': 130,
            'folding clothes': 131,
            'folding napkins': 132,
            'folding paper': 133,
            'front raises': 134,
            'frying vegetables': 135,
            'garbage collecting': 136,
            'gargling': 137,
            'getting a haircut': 138,
            'getting a tattoo': 139,
            'giving or receiving award': 140,
            'golf chipping': 141,
            'golf driving': 142,
            'golf putting': 143,
            'grinding meat': 144,
            'grooming dog': 145,
            'grooming horse': 146,
            'gymnastics tumbling': 147,
            'hammer throw': 148,
            'headbanging': 149,
            'headbutting': 150,
            'high jump': 151,
            'high kick': 152,
            'hitting baseball': 153,
            'hockey stop': 154,
            'holding snake': 155,
            'hopscotch': 156,
            'hoverboarding': 157,
            'hugging': 158,
            'hula hooping': 159,
            'hurdling': 160,
            'hurling (sport)': 161,
            'ice climbing': 162,
            'ice fishing': 163,
            'ice skating': 164,
            'ironing': 165,
            'javelin throw': 166,
            'jetskiing': 167,
            'jogging': 168,
            'juggling balls': 169,
            'juggling fire': 170,
            'juggling soccer ball': 171,
            'jumping into pool': 172,
            'jumpstyle dancing': 173,
            'kicking field goal': 174,
            'kicking soccer ball': 175,
            'kissing': 176,
            'kitesurfing': 177,
            'knitting': 178,
            'krumping': 179,
            'laughing': 180,
            'laying bricks': 181,
            'long jump': 182,
            'lunge': 183,
            'making a cake': 184,
            'making a sandwich': 185,
            'making bed': 186,
            'making jewelry': 187,
            'making pizza': 188,
            'making snowman': 189,
            'making sushi': 190,
            'making tea': 191,
            'marching': 192,
            'massaging back': 193,
            'massaging feet': 194,
            'massaging legs': 195,
            "massaging person's head": 196,
            'milking cow': 197,
            'mopping floor': 198,
            'motorcycling': 199,
            'moving furniture': 200,
            'mowing lawn': 201,
            'news anchoring': 202,
            'opening bottle': 203,
            'opening present': 204,
            'paragliding': 205,
            'parasailing': 206,
            'parkour': 207,
            'passing American football (in game)': 208,
            'passing American football (not in game)': 209,
            'peeling apples': 210,
            'peeling potatoes': 211,
            'petting animal (not cat)': 212,
            'petting cat': 213,
            'picking fruit': 214,
            'planting trees': 215,
            'plastering': 216,
            'playing accordion': 217,
            'playing badminton': 218,
            'playing bagpipes': 219,
            'playing basketball': 220,
            'playing bass guitar': 221,
            'playing cards': 222,
            'playing cello': 223,
            'playing chess': 224,
            'playing clarinet': 225,
            'playing controller': 226,
            'playing cricket': 227,
            'playing cymbals': 228,
            'playing didgeridoo': 229,
            'playing drums': 230,
            'playing flute': 231,
            'playing guitar': 232,
            'playing harmonica': 233,
            'playing harp': 234,
            'playing ice hockey': 235,
            'playing keyboard': 236,
            'playing kickball': 237,
            'playing monopoly': 238,
            'playing organ': 239,
            'playing paintball': 240,
            'playing piano': 241,
            'playing poker': 242,
            'playing recorder': 243,
            'playing saxophone': 244,
            'playing squash or racquetball': 245,
            'playing tennis': 246,
            'playing trombone': 247,
            'playing trumpet': 248,
            'playing ukulele': 249,
            'playing violin': 250,
            'playing volleyball': 251,
            'playing xylophone': 252,
            'pole vault': 253,
            'presenting weather forecast': 254,
            'pull ups': 255,
            'pumping fist': 256,
            'pumping gas': 257,
            'punching bag': 258,
            'punching person (boxing)': 259,
            'push up': 260,
            'pushing car': 261,
            'pushing cart': 262,
            'pushing wheelchair': 263,
            'reading book': 264,
            'reading newspaper': 265,
            'recording music': 266,
            'riding a bike': 267,
            'riding camel': 268,
            'riding elephant': 269,
            'riding mechanical bull': 270,
            'riding mountain bike': 271,
            'riding mule': 272,
            'riding or walking with horse': 273,
            'riding scooter': 274,
            'riding unicycle': 275,
            'ripping paper': 276,
            'robot dancing': 277,
            'rock climbing': 278,
            'rock scissors paper': 279,
            'roller skating': 280,
            'running on treadmill': 281,
            'sailing': 282,
            'salsa dancing': 283,
            'sanding floor': 284,
            'scrambling eggs': 285,
            'scuba diving': 286,
            'setting table': 287,
            'shaking hands': 288,
            'shaking head': 289,
            'sharpening knives': 290,
            'sharpening pencil': 291,
            'shaving head': 292,
            'shaving legs': 293,
            'shearing sheep': 294,
            'shining shoes': 295,
            'shooting basketball': 296,
            'shooting goal (soccer)': 297,
            'shot put': 298,
            'shoveling snow': 299,
            'shredding paper': 300,
            'shuffling cards': 301,
            'side kick': 302,
            'sign language interpreting': 303,
            'singing': 304,
            'situp': 305,
            'skateboarding': 306,
            'ski jumping': 307,
            'skiing (not slalom or crosscountry)': 308,
            'skiing crosscountry': 309,
            'skiing slalom': 310,
            'skipping rope': 311,
            'skydiving': 312,
            'slacklining': 313,
            'slapping': 314,
            'sled dog racing': 315,
            'smoking': 316,
            'smoking hookah': 317,
            'snatch weight lifting': 318,
            'sneezing': 319,
            'sniffing': 320,
            'snorkeling': 321,
            'snowboarding': 322,
            'snowkiting': 323,
            'snowmobiling': 324,
            'somersaulting': 325,
            'spinning poi': 326,
            'spray painting': 327,
            'spraying': 328,
            'springboard diving': 329,
            'squat': 330,
            'sticking tongue out': 331,
            'stomping grapes': 332,
            'stretching arm': 333,
            'stretching leg': 334,
            'strumming guitar': 335,
            'surfing crowd': 336,
            'surfing water': 337,
            'sweeping floor': 338,
            'swimming backstroke': 339,
            'swimming breast stroke': 340,
            'swimming butterfly stroke': 341,
            'swing dancing': 342,
            'swinging legs': 343,
            'swinging on something': 344,
            'sword fighting': 345,
            'tai chi': 346,
            'taking a shower': 347,
            'tango dancing': 348,
            'tap dancing': 349,
            'tapping guitar': 350,
            'tapping pen': 351,
            'tasting beer': 352,
            'tasting food': 353,
            'testifying': 354,
            'texting': 355,
            'throwing axe': 356,
            'throwing ball': 357,
            'throwing discus': 358,
            'tickling': 359,
            'tobogganing': 360,
            'tossing coin': 361,
            'tossing salad': 362,
            'training dog': 363,
            'trapezing': 364,
            'trimming or shaving beard': 365,
            'trimming trees': 366,
            'triple jump': 367,
            'tying bow tie': 368,
            'tying knot (not on a tie)': 369,
            'tying tie': 370,
            'unboxing': 371,
            'unloading truck': 372,
            'using computer': 373,
            'using remote controller (not gaming)': 374,
            'using segway': 375,
            'vault': 376,
            'waiting in line': 377,
            'walking the dog': 378,
            'washing dishes': 379,
            'washing feet': 380,
            'washing hair': 381,
            'washing hands': 382,
            'water skiing': 383,
            'water sliding': 384,
            'watering plants': 385,
            'waxing back': 386,
            'waxing chest': 387,
            'waxing eyebrows': 388,
            'waxing legs': 389,
            'weaving basket': 390,
            'welding': 391,
            'whistling': 392,
            'windsurfing': 393,
            'wrapping present': 394,
            'wrestling': 395,
            'writing': 396,
            'yawning': 397,
            'yoga': 398,
            'zumba': 399
        }
    elif dataset == 'kinetics700':
        label2id_map = {
            'abseiling': 0,
            'acting in play': 1,
            'adjusting glasses': 2,
            'air drumming': 3,
            'alligator wrestling': 4,
            'answering questions': 5,
            'applauding': 6,
            'applying cream': 7,
            'archaeological excavation': 8,
            'archery': 9,
            'arguing': 10,
            'arm wrestling': 11,
            'arranging flowers': 12,
            'arresting': 13,
            'assembling bicycle': 14,
            'assembling computer': 15,
            'attending conference': 16,
            'auctioning': 17,
            'baby waking up': 18,
            'backflip (human)': 19,
            'baking cookies': 20,
            'bandaging': 21,
            'barbequing': 22,
            'bartending': 23,
            'base jumping': 24,
            'bathing dog': 25,
            'battle rope training': 26,
            'beatboxing': 27,
            'bee keeping': 28,
            'being excited': 29,
            'being in zero gravity': 30,
            'belly dancing': 31,
            'bench pressing': 32,
            'bending back': 33,
            'bending metal': 34,
            'biking through snow': 35,
            'blasting sand': 36,
            'blending fruit': 37,
            'blowdrying hair': 38,
            'blowing bubble gum': 39,
            'blowing glass': 40,
            'blowing leaves': 41,
            'blowing nose': 42,
            'blowing out candles': 43,
            'bobsledding': 44,
            'bodysurfing': 45,
            'bookbinding': 46,
            'bottling': 47,
            'bouncing ball (not juggling)': 48,
            'bouncing on bouncy castle': 49,
            'bouncing on trampoline': 50,
            'bowling': 51,
            'braiding hair': 52,
            'breading or breadcrumbing': 53,
            'breakdancing': 54,
            'breaking boards': 55,
            'breaking glass': 56,
            'breathing fire': 57,
            'brush painting': 58,
            'brushing floor': 59,
            'brushing hair': 60,
            'brushing teeth': 61,
            'building cabinet': 62,
            'building lego': 63,
            'building sandcastle': 64,
            'building shed': 65,
            'bulldozing': 66,
            'bungee jumping': 67,
            'burping': 68,
            'busking': 69,
            'calculating': 70,
            'calligraphy': 71,
            'canoeing or kayaking': 72,
            'capoeira': 73,
            'capsizing': 74,
            'card stacking': 75,
            'card throwing': 76,
            'carrying baby': 77,
            'carrying weight': 78,
            'cartwheeling': 79,
            'carving ice': 80,
            'carving marble': 81,
            'carving pumpkin': 82,
            'carving wood with a knife': 83,
            'casting fishing line': 84,
            'catching fish': 85,
            'catching or throwing baseball': 86,
            'catching or throwing frisbee': 87,
            'catching or throwing softball': 88,
            'celebrating': 89,
            'changing gear in car': 90,
            'changing oil': 91,
            'changing wheel (not on bike)': 92,
            'chasing': 93,
            'checking tires': 94,
            'checking watch': 95,
            'cheerleading': 96,
            'chewing gum': 97,
            'chiseling stone': 98,
            'chiseling wood': 99,
            'chopping meat': 100,
            'chopping wood': 101,
            'clam digging': 102,
            'clapping': 103,
            'clay pottery making': 104,
            'clean and jerk': 105,
            'cleaning gutters': 106,
            'cleaning pool': 107,
            'cleaning shoes': 108,
            'cleaning toilet': 109,
            'cleaning windows': 110,
            'climbing a rope': 111,
            'climbing ladder': 112,
            'climbing tree': 113,
            'closing door': 114,
            'coloring in': 115,
            'combing hair': 116,
            'contact juggling': 117,
            'contorting': 118,
            'cooking chicken': 119,
            'cooking egg': 120,
            'cooking on campfire': 121,
            'cooking sausages (not on barbeque)': 122,
            'cooking scallops': 123,
            'cosplaying': 124,
            'coughing': 125,
            'counting money': 126,
            'country line dancing': 127,
            'cracking back': 128,
            'cracking knuckles': 129,
            'cracking neck': 130,
            'crawling baby': 131,
            'crocheting': 132,
            'crossing eyes': 133,
            'crossing river': 134,
            'crying': 135,
            'cumbia': 136,
            'curling (sport)': 137,
            'curling eyelashes': 138,
            'curling hair': 139,
            'cutting apple': 140,
            'cutting cake': 141,
            'cutting nails': 142,
            'cutting orange': 143,
            'cutting pineapple': 144,
            'cutting watermelon': 145,
            'dancing ballet': 146,
            'dancing charleston': 147,
            'dancing gangnam style': 148,
            'dancing macarena': 149,
            'deadlifting': 150,
            'dealing cards': 151,
            'decorating the christmas tree': 152,
            'decoupage': 153,
            'delivering mail': 154,
            'digging': 155,
            'dining': 156,
            'directing traffic': 157,
            'disc golfing': 158,
            'diving cliff': 159,
            'docking boat': 160,
            'dodgeball': 161,
            'doing aerobics': 162,
            'doing jigsaw puzzle': 163,
            'doing laundry': 164,
            'doing nails': 165,
            'doing sudoku': 166,
            'drawing': 167,
            'dribbling basketball': 168,
            'drinking shots': 169,
            'driving car': 170,
            'driving tractor': 171,
            'drooling': 172,
            'drop kicking': 173,
            'drumming fingers': 174,
            'dumpster diving': 175,
            'dunking basketball': 176,
            'dyeing eyebrows': 177,
            'dyeing hair': 178,
            'eating burger': 179,
            'eating cake': 180,
            'eating carrots': 181,
            'eating chips': 182,
            'eating doughnuts': 183,
            'eating hotdog': 184,
            'eating ice cream': 185,
            'eating nachos': 186,
            'eating spaghetti': 187,
            'eating watermelon': 188,
            'egg hunting': 189,
            'embroidering': 190,
            'entering church': 191,
            'exercising arm': 192,
            'exercising with an exercise ball': 193,
            'extinguishing fire': 194,
            'faceplanting': 195,
            'falling off bike': 196,
            'falling off chair': 197,
            'feeding birds': 198,
            'feeding fish': 199,
            'feeding goats': 200,
            'fencing (sport)': 201,
            'fidgeting': 202,
            'filling cake': 203,
            'filling eyebrows': 204,
            'finger snapping': 205,
            'fixing bicycle': 206,
            'fixing hair': 207,
            'flint knapping': 208,
            'flipping bottle': 209,
            'flipping pancake': 210,
            'fly tying': 211,
            'flying kite': 212,
            'folding clothes': 213,
            'folding napkins': 214,
            'folding paper': 215,
            'front raises': 216,
            'frying vegetables': 217,
            'gargling': 218,
            'geocaching': 219,
            'getting a haircut': 220,
            'getting a piercing': 221,
            'getting a tattoo': 222,
            'giving or receiving award': 223,
            'gold panning': 224,
            'golf chipping': 225,
            'golf driving': 226,
            'golf putting': 227,
            'gospel singing in church': 228,
            'grinding meat': 229,
            'grooming cat': 230,
            'grooming dog': 231,
            'grooming horse': 232,
            'gymnastics tumbling': 233,
            'hammer throw': 234,
            'hand washing clothes': 235,
            'head stand': 236,
            'headbanging': 237,
            'headbutting': 238,
            'helmet diving': 239,
            'herding cattle': 240,
            'high fiving': 241,
            'high jump': 242,
            'high kick': 243,
            'historical reenactment': 244,
            'hitting baseball': 245,
            'hockey stop': 246,
            'holding snake': 247,
            'home roasting coffee': 248,
            'hopscotch': 249,
            'hoverboarding': 250,
            'huddling': 251,
            'hugging (not baby)': 252,
            'hugging baby': 253,
            'hula hooping': 254,
            'hurdling': 255,
            'hurling (sport)': 256,
            'ice climbing': 257,
            'ice fishing': 258,
            'ice skating': 259,
            'ice swimming': 260,
            'inflating balloons': 261,
            'installing carpet': 262,
            'ironing': 263,
            'ironing hair': 264,
            'javelin throw': 265,
            'jaywalking': 266,
            'jetskiing': 267,
            'jogging': 268,
            'juggling balls': 269,
            'juggling fire': 270,
            'juggling soccer ball': 271,
            'jumping bicycle': 272,
            'jumping into pool': 273,
            'jumping jacks': 274,
            'jumping sofa': 275,
            'jumpstyle dancing': 276,
            'karaoke': 277,
            'kicking field goal': 278,
            'kicking soccer ball': 279,
            'kissing': 280,
            'kitesurfing': 281,
            'knitting': 282,
            'krumping': 283,
            'land sailing': 284,
            'laughing': 285,
            'lawn mower racing': 286,
            'laying bricks': 287,
            'laying concrete': 288,
            'laying decking': 289,
            'laying stone': 290,
            'laying tiles': 291,
            'leatherworking': 292,
            'letting go of balloon': 293,
            'licking': 294,
            'lifting hat': 295,
            'lighting candle': 296,
            'lighting fire': 297,
            'listening with headphones': 298,
            'lock picking': 299,
            'long jump': 300,
            'longboarding': 301,
            'looking at phone': 302,
            'looking in mirror': 303,
            'luge': 304,
            'lunge': 305,
            'making a cake': 306,
            'making a sandwich': 307,
            'making balloon shapes': 308,
            'making bubbles': 309,
            'making cheese': 310,
            'making horseshoes': 311,
            'making jewelry': 312,
            'making latte art': 313,
            'making paper aeroplanes': 314,
            'making pizza': 315,
            'making slime': 316,
            'making snowman': 317,
            'making sushi': 318,
            'making tea': 319,
            'making the bed': 320,
            'marching': 321,
            'marriage proposal': 322,
            'massaging back': 323,
            'massaging feet': 324,
            'massaging legs': 325,
            'massaging neck': 326,
            'massaging person\'s head': 327,
            'metal detecting': 328,
            'milking cow': 329,
            'milking goat': 330,
            'mixing colours': 331,
            'moon walking': 332,
            'mopping floor': 333,
            'mosh pit dancing': 334,
            'motorcycling': 335,
            'mountain climber (exercise)': 336,
            'moving baby': 337,
            'moving child': 338,
            'moving furniture': 339,
            'mowing lawn': 340,
            'mushroom foraging': 341,
            'needle felting': 342,
            'news anchoring': 343,
            'opening bottle (not wine)': 344,
            'opening coconuts': 345,
            'opening door': 346,
            'opening present': 347,
            'opening refrigerator': 348,
            'opening wine bottle': 349,
            'packing': 350,
            'paragliding': 351,
            'parasailing': 352,
            'parkour': 353,
            'passing American football (in game)': 354,
            'passing American football (not in game)': 355,
            'passing soccer ball': 356,
            'peeling apples': 357,
            'peeling banana': 358,
            'peeling potatoes': 359,
            'person collecting garbage': 360,
            'petting animal (not cat)': 361,
            'petting cat': 362,
            'petting horse': 363,
            'photobombing': 364,
            'photocopying': 365,
            'picking apples': 366,
            'picking blueberries': 367,
            'pillow fight': 368,
            'pinching': 369,
            'pirouetting': 370,
            'planing wood': 371,
            'planting trees': 372,
            'plastering': 373,
            'playing accordion': 374,
            'playing american football': 375,
            'playing badminton': 376,
            'playing bagpipes': 377,
            'playing basketball': 378,
            'playing bass guitar': 379,
            'playing beer pong': 380,
            'playing billiards': 381,
            'playing blackjack': 382,
            'playing cards': 383,
            'playing cello': 384,
            'playing checkers': 385,
            'playing chess': 386,
            'playing clarinet': 387,
            'playing controller': 388,
            'playing cricket': 389,
            'playing cymbals': 390,
            'playing darts': 391,
            'playing didgeridoo': 392,
            'playing dominoes': 393,
            'playing drums': 394,
            'playing field hockey': 395,
            'playing flute': 396,
            'playing gong': 397,
            'playing guitar': 398,
            'playing hand clapping games': 399,
            'playing harmonica': 400,
            'playing harp': 401,
            'playing ice hockey': 402,
            'playing keyboard': 403,
            'playing kickball': 404,
            'playing laser tag': 405,
            'playing lute': 406,
            'playing mahjong': 407,
            'playing maracas': 408,
            'playing marbles': 409,
            'playing monopoly': 410,
            'playing netball': 411,
            'playing nose flute': 412,
            'playing oboe': 413,
            'playing ocarina': 414,
            'playing organ': 415,
            'playing paintball': 416,
            'playing pan pipes': 417,
            'playing piano': 418,
            'playing piccolo': 419,
            'playing pinball': 420,
            'playing ping pong': 421,
            'playing poker': 422,
            'playing polo': 423,
            'playing recorder': 424,
            'playing road hockey': 425,
            'playing rounders': 426,
            'playing rubiks cube': 427,
            'playing saxophone': 428,
            'playing scrabble': 429,
            'playing shuffleboard': 430,
            'playing slot machine': 431,
            'playing squash or racquetball': 432,
            'playing tennis': 433,
            'playing trombone': 434,
            'playing trumpet': 435,
            'playing ukulele': 436,
            'playing violin': 437,
            'playing volleyball': 438,
            'playing with trains': 439,
            'playing xylophone': 440,
            'poaching eggs': 441,
            'poking bellybutton': 442,
            'pole vault': 443,
            'polishing furniture': 444,
            'polishing metal': 445,
            'popping balloons': 446,
            'pouring beer': 447,
            'pouring milk': 448,
            'pouring wine': 449,
            'preparing salad': 450,
            'presenting weather forecast': 451,
            'pretending to be a statue': 452,
            'pull ups': 453,
            'pulling espresso shot': 454,
            'pulling rope (game)': 455,
            'pumping fist': 456,
            'pumping gas': 457,
            'punching bag': 458,
            'punching person (boxing)': 459,
            'push up': 460,
            'pushing car': 461,
            'pushing cart': 462,
            'pushing wheelbarrow': 463,
            'pushing wheelchair': 464,
            'putting in contact lenses': 465,
            'putting on eyeliner': 466,
            'putting on foundation': 467,
            'putting on lipstick': 468,
            'putting on mascara': 469,
            'putting on sari': 470,
            'putting on shoes': 471,
            'putting wallpaper on wall': 472,
            'raising eyebrows': 473,
            'reading book': 474,
            'reading newspaper': 475,
            'recording music': 476,
            'repairing puncture': 477,
            'riding a bike': 478,
            'riding camel': 479,
            'riding elephant': 480,
            'riding mechanical bull': 481,
            'riding mule': 482,
            'riding or walking with horse': 483,
            'riding scooter': 484,
            'riding snow blower': 485,
            'riding unicycle': 486,
            'ripping paper': 487,
            'roasting marshmallows': 488,
            'roasting pig': 489,
            'robot dancing': 490,
            'rock climbing': 491,
            'rock scissors paper': 492,
            'roller skating': 493,
            'rolling eyes': 494,
            'rolling pastry': 495,
            'rope pushdown': 496,
            'running on treadmill': 497,
            'sailing': 498,
            'salsa dancing': 499,
            'saluting': 500,
            'sanding floor': 501,
            'sanding wood': 502,
            'sausage making': 503,
            'sawing wood': 504,
            'scrambling eggs': 505,
            'scrapbooking': 506,
            'scrubbing face': 507,
            'scuba diving': 508,
            'seasoning food': 509,
            'separating eggs': 510,
            'setting table': 511,
            'sewing': 512,
            'shaking hands': 513,
            'shaking head': 514,
            'shaping bread dough': 515,
            'sharpening knives': 516,
            'sharpening pencil': 517,
            'shaving head': 518,
            'shaving legs': 519,
            'shearing sheep': 520,
            'shining flashlight': 521,
            'shining shoes': 522,
            'shoot dance': 523,
            'shooting basketball': 524,
            'shooting goal (soccer)': 525,
            'shooting off fireworks': 526,
            'shopping': 527,
            'shot put': 528,
            'shouting': 529,
            'shoveling snow': 530,
            'shredding paper': 531,
            'shucking oysters': 532,
            'shuffling cards': 533,
            'shuffling feet': 534,
            'side kick': 535,
            'sieving': 536,
            'sign language interpreting': 537,
            'silent disco': 538,
            'singing': 539,
            'sipping cup': 540,
            'situp': 541,
            'skateboarding': 542,
            'ski ballet': 543,
            'ski jumping': 544,
            'skiing crosscountry': 545,
            'skiing mono': 546,
            'skiing slalom': 547,
            'skipping rope': 548,
            'skipping stone': 549,
            'skydiving': 550,
            'slacklining': 551,
            'slapping': 552,
            'sled dog racing': 553,
            'sleeping': 554,
            'slicing onion': 555,
            'smashing': 556,
            'smelling feet': 557,
            'smoking': 558,
            'smoking hookah': 559,
            'smoking pipe': 560,
            'snatch weight lifting': 561,
            'sneezing': 562,
            'snorkeling': 563,
            'snowboarding': 564,
            'snowkiting': 565,
            'snowmobiling': 566,
            'somersaulting': 567,
            'spelunking': 568,
            'spinning plates': 569,
            'spinning poi': 570,
            'splashing water': 571,
            'spray painting': 572,
            'spraying': 573,
            'springboard diving': 574,
            'square dancing': 575,
            'squat': 576,
            'squeezing orange': 577,
            'stacking cups': 578,
            'stacking dice': 579,
            'standing on hands': 580,
            'staring': 581,
            'steer roping': 582,
            'steering car': 583,
            'sticking tongue out': 584,
            'stomping grapes': 585,
            'stretching arm': 586,
            'stretching leg': 587,
            'sucking lolly': 588,
            'surfing crowd': 589,
            'surfing water': 590,
            'surveying': 591,
            'sweeping floor': 592,
            'swimming backstroke': 593,
            'swimming breast stroke': 594,
            'swimming butterfly stroke': 595,
            'swimming front crawl': 596,
            'swimming with dolphins': 597,
            'swimming with sharks': 598,
            'swing dancing': 599,
            'swinging baseball bat': 600,
            'swinging on something': 601,
            'sword fighting': 602,
            'sword swallowing': 603,
            'tackling': 604,
            'tagging graffiti': 605,
            'tai chi': 606,
            'taking photo': 607,
            'talking on cell phone': 608,
            'tango dancing': 609,
            'tap dancing': 610,
            'tapping guitar': 611,
            'tapping pen': 612,
            'tasting beer': 613,
            'tasting food': 614,
            'tasting wine': 615,
            'testifying': 616,
            'texting': 617,
            'threading needle': 618,
            'throwing axe': 619,
            'throwing ball (not baseball or American football)': 620,
            'throwing discus': 621,
            'throwing knife': 622,
            'throwing snowballs': 623,
            'throwing tantrum': 624,
            'throwing water balloon': 625,
            'tickling': 626,
            'tie dying': 627,
            'tightrope walking': 628,
            'tiptoeing': 629,
            'tobogganing': 630,
            'tossing coin': 631,
            'tossing salad': 632,
            'training dog': 633,
            'trapezing': 634,
            'treating wood': 635,
            'trimming or shaving beard': 636,
            'trimming shrubs': 637,
            'trimming trees': 638,
            'triple jump': 639,
            'twiddling fingers': 640,
            'tying bow tie': 641,
            'tying knot (not on a tie)': 642,
            'tying necktie': 643,
            'tying shoe laces': 644,
            'unboxing': 645,
            'uncorking champagne': 646,
            'unloading truck': 647,
            'using a microscope': 648,
            'using a paint roller': 649,
            'using a power drill': 650,
            'using a sledge hammer': 651,
            'using a wrench': 652,
            'using atm': 653,
            'using bagging machine': 654,
            'using circular saw': 655,
            'using inhaler': 656,
            'using megaphone': 657,
            'using puppets': 658,
            'using remote controller (not gaming)': 659,
            'using segway': 660,
            'vacuuming car': 661,
            'vacuuming floor': 662,
            'visiting the zoo': 663,
            'wading through mud': 664,
            'wading through water': 665,
            'waiting in line': 666,
            'waking up': 667,
            'walking on stilts': 668,
            'walking the dog': 669,
            'walking through snow': 670,
            'walking with crutches': 671,
            'washing dishes': 672,
            'washing feet': 673,
            'washing hair': 674,
            'washing hands': 675,
            'watching tv': 676,
            'water skiing': 677,
            'water sliding': 678,
            'watering plants': 679,
            'waving hand': 680,
            'waxing armpits': 681,
            'waxing back': 682,
            'waxing chest': 683,
            'waxing eyebrows': 684,
            'waxing legs': 685,
            'weaving basket': 686,
            'weaving fabric': 687,
            'welding': 688,
            'whistling': 689,
            'windsurfing': 690,
            'winking': 691,
            'wood burning (art)': 692,
            'wrapping present': 693,
            'wrestling': 694,
            'writing': 695,
            'yarn spinning': 696,
            'yawning': 697,
            'yoga': 698,
            'zumba': 699
        }
    else:
        print("You have to chose an appropriate dataset name.")
        sys.exit(1)

    return label2id_map