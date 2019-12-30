# 跟踪游戏统计信息的新类

class GameStats():

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏一开始处于非活动状态
        self.game_active = False
        self.high_score_file_name = 'high_score.txt'
        # 在任何情况下都不应该重置最高得分
        self.high_score = 0
        with open(self.high_score_file_name, "r") as file_object:
            high_score_last =  file_object.read()
            if high_score_last:
                self.high_score = int(high_score_last)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1