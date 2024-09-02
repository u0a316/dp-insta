#!/usr/bin/env python3

import instaloader
 
ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")
 
ig.download_profile(dp , profile_pic_only=True)
