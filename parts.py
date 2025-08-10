import pygame


class Part:
    def __init__(self, worth, cost, r_attack_bonus, m_attack_bonus, armor_bonus, speed_bonus):
        self.worth = worth
        self.cost = cost
        self.r_attack_bonus = r_attack_bonus
        self.m_attack_bonus = m_attack_bonus
        self.armor_bonus = armor_bonus
        self.speed_bonus = speed_bonus
