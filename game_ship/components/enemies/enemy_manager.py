from game_ship.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def add_enemy(self): 
        if len(self.enemies) < 3:
            enemy = Enemy()
            self.enemies.append(enemy)

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)