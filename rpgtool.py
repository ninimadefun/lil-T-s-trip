import sys, pygame

size = width, height = 1024, 731
sprite_size = 227, 243
black = 0, 0, 0
title_bg = 220, 220, 220
message_bg = 220, 220, 220
question_bg = 255, 200, 200

class Scene(object):
    def __init__(self, size, sprite_size=sprite_size,
                 font_color=black,
                 title_bg=title_bg,
                 message_bg=message_bg,
                 question_bg=question_bg):
        self.size = size
        self.sprite_size = sprite_size
        self.font_color = font_color
        self.title_bg = title_bg
        self.message_bg = message_bg
        self.question_bg = question_bg

        self._init_screen()

        self.should_update = False
        pass

    def load_background(self, filename):
        background = pygame.image.load(filename)
        self.background = pygame.transform.scale(background, size)
        self.backgroundrect = self.background.get_rect()
        self.should_update = True
        return self.background, self.backgroundrect

    def load_sprite(self, filename):
        sprite = pygame.image.load(filename)
        self.sprite = pygame.transform.scale(sprite, self.sprite_size)
        self.spriterect = self.sprite.get_rect().move((700, 100))
        self.should_update = True
        pass

    def set_title(self, title):
        self.title = title
        self.should_update = True
        pass

    def set_message(self, message):
        self.message = message
        self.should_update = True
        pass

    def wait(self):
        key = []
        def key_handler(_self, event):
            if event.type == pygame.KEYDOWN:
                key.append(pygame.key.name(event.key))
                pass
            pass
        while len(key) == 0:
            self._loop_inner(key_handler)
            pass
        return key[-1]

    def ask_user(self, question):
        self.question = question
        self.should_update = True

        key = self.wait()

        del self.question
        self.should_update = True
        return key

    def _draw_title(self):
        screen = self.screen
        font_title = self.font_title

        title_img = font_title.render(self.title, True, self.font_color)
        rect = title_img.get_rect()
        rect = rect.move([100, 20])
        pygame.draw.rect(screen, self.title_bg, rect)
        screen.blit(title_img, rect)
        pass

    def _draw_message(self):
        message = self.message
        screen = self.screen
        font = self.font_message
        for lineno, line in enumerate(message.split('\n')):
            line_img = font.render(line, True, self.font_color)
            rect = line_img.get_rect()
            rect = rect.move([100, 100 + lineno * 30])
            pygame.draw.rect(screen, self.message_bg, rect)
            screen.blit(line_img, rect)
            pass
        pass

    def _draw_question(self):
        if (not hasattr(self, 'question')) or (not self.question):
            return

        question = self.question
        font = self.font_question
        screen = self.screen
        for lineno, line in enumerate(question.split('\n')):
            line_img = font.render(line, True, self.font_color)
            rect = line_img.get_rect()
            rect = rect.move([100, 500 + lineno * 30])
            pygame.draw.rect(screen, self.question_bg, rect)
            screen.blit(line_img, rect)
            pass
        pass

    def update_screen(self):
        screen = self.screen
        font_message = self.font_message

        screen.fill(black)
        screen.blit(self.background, self.backgroundrect)

        screen.blit(self.sprite, self.spriterect)

        self._draw_title()
        self._draw_message()
        self._draw_question()

        pygame.display.flip()

        self.should_update = False
        pass

    def _handle_event(self, event, event_handler):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event_handler:
            event_handler(self, event)
            pass
        pass

    def _init_screen(self):
        pygame.init()

        screen = pygame.display.set_mode(self.size)
        pygame.font.init()
        dflfont = pygame.font.get_default_font()
        font_title = pygame.font.Font(dflfont, 32)
        font_message = pygame.font.Font(dflfont, 20)
        font_question = pygame.font.Font(dflfont, 20)

        self.screen = screen
        self.font_title = font_title
        self.font_message = font_message
        self.font_question = font_question
        pass

    def _loop_inner(self, event_handler):
        if self.should_update:
            self.update_screen()
            pass

        event = pygame.event.wait()
        if event.type != pygame.NOEVENT:
            self._handle_event(event, event_handler)
            for event in pygame.event.get():
                self._handle_event(event, event_handler)
                pass
            pass

        if self.should_update:
            self.update_screen()
            pass
        pass
    pass


if __name__ == '__main__':
    background_filenames = ['NiboyMt.png', 'RanchoBernardo-color.png']
    titles = ['Niboy Mt.', 'Rancho Bernardo']
    messages = [
        '''Niboy Mt is a beautiful place.
Everyone love it.''',
        '''Rancho Bernardo is a lovely place.
We visit it a lot!'''
    ]
    
    sceneidx = 0

    def set_scene(scene, idx):
        bgfilename = background_filenames[idx]
        scene.load_background(bgfilename)

        title = titles[idx]
        scene.set_title(title)

        message = messages[idx]
        scene.set_message(message)
        pass

    scene = Scene(size)
    scene.load_sprite('alpha-lil-T.png')
    set_scene(scene, sceneidx)
    scene.ask_user('How are you?')
    scene.ask_user('Really?')

    sceneidx = 1
    set_scene(scene, sceneidx)
    while scene.wait() != 'q':
        pass
    pass

