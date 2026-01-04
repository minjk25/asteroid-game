import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        #print(self.rotation) 

    def update(self, dt):
        #time passes
        self.shot_cooldown_timer -= dt

        # to check self.shot_cooldown_timer
        #print("cooldown:", self.shot_cooldown_timer)

        # read keys and move/rotate
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #print("A pressed, rotating left")
            self.rotate(-dt)
        if keys[pygame.K_d]:
            #print("D pressed, rotating right")
            self.rotate(dt)
        if keys[pygame.K_w]:
            #print("W pressed, moving forward")
            self.move(dt)
        if keys[pygame.K_s]:
            #print("S pressed, moving backward")
            self.move(-dt)

        # shooting request
        # 7. handle the spacebar (pygame.K_SPACE) and call the shoot method when it's pressed.
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        
        # to check when you press space bar and it resrt self.shot_cooldown_timer to 0.3
        #print("Shooting! cooldown reset to", PLAYER_SHOOT_COOLDOWN_SECONDS)

        # 1. get x, y from the player’s position
        # 2. create bullet = Shot(x, y)
        bullet = Shot(self.position.x, self.position.y)

        # 3. make a direction vector = pygame.Vector2(0, 1)
        # 4. rotate it using the player’s angle (whatever attribute you use)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)

        # 5. multiply direction by PLAYER_SHOOT_SPEED
        # 6. assign that to bullet.velocity
        bullet.velocity = direction * PLAYER_SHOOT_SPEED

        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        
