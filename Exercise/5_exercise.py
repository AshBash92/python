import matplotlib.colors as mcl
import random

def q_color(color):
    # Get a list of the named colors
    colors = mcl.CSS4_COLORS

    while True:
        if color in colors:
            print(f"Great choice, {color} is an excellent color!")
            return color
        else:
            color = input("\nThat color isn't cool enough to be on the list. Please try again.\n").lower()

def q_noun(noun):

    animals = [
        'crow', 'puma', 'manatee', 'vole', 'dove', 'skunk', 'beaver', 'capybara', 'stingray', 'wombat', 'lark', 'cockroach', 'herring', 'tenrec', 'kiwi', 'opossum', 'weasel', 'jackrabbit', 'eel', 'finch', 'stork', 'hedgehog', 'marmoset', 'cat', 'bobcat', 'goat', 'moth', 'swan', 'bison', 'stoat', 'komodo dragon', 'chinchilla', 'grouse', 'mink', 'elephant', 'snake', 'guanaco', 'cattle', 'orangutan', 'ferret', 'wolf', 'penguin', 'monkey', 'hyena', 'bighorn sheep', 'muskrat', 'fox', 'alligator', 'caterpillar', 'mouse', 'bear', 'rhinoceros', 'hippopotamus', 'yak', 'seahorse', 'hummingbird', 'kingfisher', 'sea lion', 'seagull', 'pangolin', 'boar', 'crane', 'kite', 'albatross', 'lion', 'newt', 'llama', 'wildcat', 'mandrill', 'iguana', 'raven', 'ox', 'sandpiper', 'partridge', 'buffalo', 'locust', 'salmon', 'scorpion', 'hamster', 'dragonfly', 'toucan', 'magpie', 'ibex', 'emu', 'chimpanzee', 'turtle', 'caribou', 'marmot', 'dog', 'kangaroo rat', 'camel', 'crab', 'hare', 'mallard', 'sheep', 'koala', 'anteater', 'lemur', 'cheetah', 'dolphin', 'antelope', 'snail', 'flamingo', 'rabbit', 'sparrow', 'lemming', 'aardvark', 'moose', 'whale', 'bee', 'chamois', 'kinkajou', 'serval', 'barracuda', 'gnu', 'turkey', 'orca', 'wild dog', 'snow leopard', 'donkey', 'peacock', 'armadillo', 'civet', 'jay', 'condor', 'gorilla', 'gnat', 'owl', 'reindeer', 'tarantula', 'deer', 'louse', 'cougar', 'rattlesnake', 'ibis', 'yabby', 'loon', 'jackal', 'wolverine', 'ring-tailed lemur', 'cobra', 'cuckoo', 'echidna', 'peccary', 'rat', 'zebra', 'warthog', 'jellyfish', 'kitten', 'lizard', 'frog', 'gull', 'lynx', 'woodpecker', 'baboon', 'chameleon', 'starfish', 'falcon', 'hornet', 'seal', 'tree kangaroo', 'grasshopper', 'pelican', 'spider', 'robin', 'wildebeest', 'giraffe', 'rooster', 'fish', 'oyster', 'horse', 'panda', 'parakeet', 'kangaroo', 'macaw', 'elk', 'cod', 'gazelle', 'sardine', 'salamander', 'pheasant', 'chipmunk', 'butterfly', 'raccoon dog', 'badger', 'crocodile', 'narwhal', 'squirrel', 'parrot', 'heron', 'otter', 'mole', 'mongoose', 'vulture', 'octopus', 'alpaca', 'guinea pig', 'pig', 'shark', 'worm', 'ostrich', 'walrus', 'canary', 'mule', 'termite', 'tiger', 'hawk', 'goose', 'panther', 'toad', 'nightingale', 'duck', 'quail', 'red fox', 'tapir', 'ant', 'cow', 'coyote', 'jaguar', 'mosquito', 'leopard', 'ladybug', 'pigeon', 'ape', 'python', 'raccoon', 'fly', 'chicken', 'sloth', 'bat', 'lobster', 'eagle', 'meerkat', "axolotl", "Binturong" , "Capybara" , "Civet" , "Dassie Rat" , "Fennec Fox" , "Genet" , "Hognose Snake" , "Kinkajou" , "Lamprey" , "Numbat" , "Pangolin" , "Quokka" , "Slow Loris" , "Tasmanian Devil" , "Uakari" , "Vaquita"
    ]

    #There's 275 list of things, but too lazy to skim it down
    things = [
    'word', 'camera', 'knife', 'email', 'bicycle', 'headphones', 'nutrition', 'laundry basket', 'zipper', 'watch', 'gloves', 'rolling pin', 'speaker', 'economics', 'management', 'drawing', 'cartoon', 'balloon', 'sentence', 'cell phone', 'cup', 'ice cream scoop', 'phone charger', 'screwdriver', 'dedication', 'garden hose', 'jacket', 'physical therapy', 'hairbrush', 'surfboard', 'board game', 'plant', 'veterinary medicine', 'laptop', 'soap', 'map', 'umbrella', 'passport', 'television', 'mixing bowl', 'table of contents', 'electric fan', 'accounting', 'phone', 'soccer ball', 'hat', 'recipe', 'history', 'tennis racket', 'sweater', 'print', 'toothpaste', 'scanner', 'lamp', 'pencil case', 'thermometer', 'helmet', 'guitar', 'shirt', 'invitation', 'mathematics', 'paintbrush', 'detergent', 'nursing', 'necklace', 'postage stamp', 'pen', 'pilates', 'frying pan', 'camera bag', 'ticket', 'painting', 'sociology', 'dentistry', 'receipt', 'medicine', 'architecture', 'dance', 'postcard', 'resume', 'sponge', 'radio', 'list', 'shampoo', 'radio show', 'chapter', 'water bottle', 'boot', 'philosophy', 'wallet', 'coin', 'banknote', 'sun glasses', 'boombox', 'calculator', 'bowling ball', 'skateboard', 'basketball', 'bag', 'oven', 'stopwatch', 'sun hat', 'flyer', 'credit card', 'comic strip', 'music', 'law', 'crayons', 'rubber duck', 'theater', 'motorcycle', 'picture frame', 'shorts', 'newspaper', 'finance', 'backpack', 'rake', 'desk', 'flashlight', 'certificate', 'coffee mug', 'dumbbells', 'sandals', 'flower vase', 'opera', 'skirt', 'barbecue grill', 'lotion', 'occupational therapy', 'air conditioner', 'clock', 'sound', 'installation', 'towel', 'report', 'pool cue', 'calendar', 'mop', 'book', 'pants', 'presentation', 'pillow', 'money clip', 'stamp', 'photograph', 'shoe', 'cooler', 'table', 'flag', 'nail clippers', 'rug', 'letter', 'kettle', 'microwave', 'perfume', 'introduction', 'couch', 'wheelbarrow', 'blanket', 'beach ball', 'fork', 'graph', 'chart', 'drill', 'psychology', 'marketing', 'index', 'podcast', 'vacuum cleaner', 'mouse', 'memorandum', 'section', 'mirror', 'chess board', 'dress', 'scarf', 'yoga mat', 'diary', 'printer', 'candle', 'speech therapy', 'cover letter', 'ski', 'airplane', 'plate', 'flip flops', 'rope', 'notebook', 'shovel', 'bottle', 'text message', 'pencil', 'suitcase', 'ipad', 'oven mitt', 'toaster', 'web series', 'bottle opener', 'paragraph', 'song', 'keychain', 'poster', 'laptop case', 'key', 'performance art', 'invoice', 'lawn mower', 'remote control', 'acknowledgments', 'booklet', 'bandana', 'plastic bag', 'sunglasses', 'underwear', 'paper clip', 'microphone', 'headphone', 'swimming', 'computer', 'foreword', 'chair', 'envelope', 'vacuum', 'sculpture', 'mp3 player', 'toothbrush', 'washing machine', 'comb', 'blender', 'keyboard', 'television show', 'hammock', 'syllable', 'globe', 'political science', 'ring', 'magazine', 'tie', 'socks', 'heater', 'slippers', 'animation', 'fan', 'razor', 'spoon', 'menu', 'brochure', 'glasses', 'business card', 'bracelet', 'toilet brush', 'pliers', 'punctuation mark', 'purse', 'contract', 'epilogue', 'fridge', 'earrings', 'science', 'belt', 'teapot', 'comic book', 'exercise', 'bibliography', 'title page', 'spatula', 'prologue', 'stapler', 'binoculars', 'movie', 'earphones', 'footnote', 'journal', 'engineering', 'yoga'
    ]

    rando = random.randint(0, 250)

    while True:
        if noun == "animals" or noun == "things":
            print(f"\nYeah, I like {noun} too.")

            mapping = {
                "animals": animals[rando],
                "things": things[rando],
            }

            new_noun = mapping.get(noun)
            return new_noun
        else:
            noun = input("\nThat answer doesn't sound right. Please try again.\n").lower()

print("\n\n\nWelcome to the User Name Generator.")

# choice = input('''\nWould you like to take a quiz to generate the name or would you like to skip?:
# \nTake Quiz, type "1"
# Skip Quiz, type "0"
# ''')

#QUIZ
color = input("\nWhat is your favorite color?\n").lower()
q_color(color)

noun = input("\nWhich do you prefer more? Animals or things?\n").lower()
noun = q_noun(noun)

print("Your username should be: " + color + " " + noun)

# numbers = input("\nWould you like to include numbers? (y/n)\n").lower

# special = input("\nWould you like to include special characters? (y/n)\n").lower