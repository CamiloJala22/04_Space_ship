from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    def add_enemy(self): 
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemy_2 = Enemy()
            enemy_3 = Enemy()
            self.enemies.append(enemy)
            self.enemies.append(enemy_2)
            self.enemies.append(enemy_3)

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)