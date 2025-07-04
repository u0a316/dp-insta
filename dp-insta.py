#!/usr/bin/env python3

import instaloader
 
ig = instaloader.Instaloader() # aliasing module to ig
dp = input("Enter Insta username : ") # create input()
 
ig.download_profile(dp , profile_pic_only=True) # proccess input to make it download work
