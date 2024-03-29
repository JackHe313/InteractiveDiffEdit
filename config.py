import argparse

parser = argparse.ArgumentParser(description="Run Stable Diffusion Diff Edit with command line arguments.")
parser.add_argument("--img_url", '-i', type=str, default='', help="URL of the image to edit.")
parser.add_argument("--target_prompt", '-t', type=str, help="Prompt for the target image.")
parser.add_argument("--source_prompt", '-p', type=str, default=None, help="Optional prompt for the source image.")
parser.add_argument("--save_path", '-s', type=str, default=None, help="Optional path to save the edited image.")
parser.add_argument("--device", '-d', type=str, default="cuda:0", help="Device to run the model on.")
parser.add_argument("--seg_prompt", '-sp', action='store_true', help="Boolean flag to indicate if the target_prompt is a segment prompt.")
parser.add_argument("--seed", type=int, default=0, help="Seed for the random number generator.")
args = parser.parse_args()
FLAGS = args