#!/usr/bin/env python
"""KhtEditor a source code editor by Khertan"""
try:
    from khweeteur import Khweeteur
except:
    from khweeteur_experimental import Khweeteur
import sys

if __name__ == '__main__':
    sys.exit(Khweeteur().exec_())
