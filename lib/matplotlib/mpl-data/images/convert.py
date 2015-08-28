import glob
import subprocess

for filename in glob.glob('*.svg'):
    print('inkscape {input_file} --export-width=48 --export-height=48 --export-png={output_file}'.format(input_file=filename,
                                                                    output_file=filename.replace('.svg', '_48pix.png')))
    
    
    
        #
    # #!/bin/bash
    #
    # # Remove old files
    # rm generated/*
    #
    # # Convert form Inkscape SVG to PNG
    # inkscape astropy_logo.svg --export-png=generated/astropy_logo.png
    # inkscape astropy_logo_linkout.svg --export-png=generated/astropy_logo_linkout.png
    # inkscape astropy_logo_docs.svg --export-png=generated/astropy_logo_docs.png
    # inkscape astropy_logo_small.svg --export-png=generated/astropy_logo_small.png
    # inkscape astropy_logo_word.svg --export-png=generated/astropy_logo_word.png
    # inkscape dmg_background.svg --export-dpi=72 --export-png=generated/dmg_background.png
    # inkscape wininst_background.svg --export-png=generated/wininst_background.png
    # inkscape astropy_logo_notext.svg --export-png=generated/astropy_logo_notext.png
    # inkscape astropy_powered.svg --export-png=generated/astropy_powered.png
    # inkscape astropy_powered_white.svg --export-png=generated/astropy_powered_white.png
    #
    # # Convert form Inkscape SVG to Plain SVG (for web use)
    # inkscape astropy_logo.svg --export-plain-svg=generated/astropy_logo_plain.svg
    # inkscape astropy_logo_linkout.svg --export-plain-svg=generated/astropy_logo_linkout_plain.svg
    # inkscape astropy_logo_docs.svg --export-plain-svg=generated/astropy_logo_docs_plain.svg
    # inkscape astropy_logo_small.svg --export-plain-svg=generated/astropy_logo_small_plain.svg
    # inkscape astropy_logo_word.svg --export-plain-svg=generated/astropy_logo_word_plain.svg
    #