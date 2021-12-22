#!/usr/bin/env python3

import os
import json
import random

class Dice:
    def __init__(self):
        self.content = []

    def check(self, content):
        score = 0
        checks = [
            {
                "name" : "size",
                "result" : self.size(content)
            },
            {
                "name" : "duplicate",
                "result" : self.duplicate(content)
            }
        ]

        for check in checks:
            if (check["result"] == False):
                print("Check '{}' failed".format(check["name"]))
            else:
                score += 1
        if (score == len(checks)):
            return (True)
        return (False)

    def load(self, content):
        if (self.check(content) == True):
            self.content = content
        else:
            print("content not set")

    def size(self, content):
        if (content != None):
            return (True)
        return (False)

    def duplicate(self, content):
        previous = []

        for data in content:
            if (data in previous):
                return (False)
        return (True)

    def run(self):
        return (self.content[random.randint(0, len(self.content) - 1)])

class Core:
    def __init__(self):
        self.dices = []
        self.settings = {
            "path" : "settings.json",
            "content" : None
        }

        self.run()

    def load(self):
        if (self.check() == True):
            try:
                with open(self.settings["path"], 'r') as f:
                    self.settings["content"] = json.load(f)
                return (True)
            except Exception as ex:
                print(ex)
                return (False)
        else:
            print("settings file '{}' not found".format(self.settings["path"]))
            return (False)

    def check(self):
        return (os.path.isfile(self.settings["path"]))

    def create(self):
        for dice in self.settings["content"]["dices"]:
            self.dices.append({
                "name" : dice["name"],
                "content" : dice["content"],
                "object" : Dice()
            })

    def run(self):
        if (self.load() == True):
            self.create()
            for dice in self.dices:
                dice["object"].load(dice["content"])
                print("{}: {}".format(
                    dice["name"],
                    dice["object"].run()
                ))

if (__name__ == "__main__"):
    Core()
