from discord.ext import commands
from discord import app_commands
from discord import Embed, Interaction
from enum import Enum

class SoulCup(commands.Cog):
    class Challenges(Enum):
        PATIENCE = "Réaliser un Wipeout (Fullteam) en shark dans le camp adverse."
        JUSTICE = "Condition secrètes"
        PERSEVERANCE = "Être mené de 75% de l'objectif ar l'adversaire et réussir à remonter et gagner la manche"
        GENTILESSE = "Un membre de l’équipe doit faire 2200 p. d’encrage ou plus en une game"
        BRAVOURE = "Mettre quatre Super Palourdes en un push"
        INTEGRITE = "Ne pas se prendre un Wipeout de tout le match"
        DETERMINATION = "Être mené 3-0 et remonter à 4-3"
        HAINE = "Un joueur doit faire plus d’éliminations que la somme des kills de ses coéquipiers en une manche"

        def __init__(self, challenge):
            self.challenge = challenge
        @property
        def challenge_name(self):
            return self.challenge.name
        @property
        def challenge_value(self):
            return self.challenge.value

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="defi_saison", description="Affiche les défis de la saison actuelle de la SoulCup")
    async def show_season_challenge(self, interaction: Interaction)-> None:
        description = []

        for challenge in SoulCup.Challenges:
            description += '\n {} {}'.format(f'**{challenge.name.lower().capitalize()}:**', challenge.value)

        embed = Embed(title="Les défis de la saison actuelle", description=''.join(description))
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(SoulCup(bot))