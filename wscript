out = 'build/waf_build'

def options(opt):
    opt.load('compiler_c')

def configure(conf):
    conf.load('compiler_c')

def build(bld):
	# Simulation library.
    bld.stlib(source=[
		'SDL_gfx/SDL_rotozoom.c',
		'SDL_gfx/SDL_gfxPrimitives.c',
		'SDL_gfx/SDL_gfxBlitFunc.c',
		'local/render.c',
		'local/scrolllayer.c',
		'local/layer.c',
		'local/jsmn.c',
		'local/simdata.c',
		'local/buttons.c',
		'local/main.c',
		'local/pebble_os.c',
		'local/font.c',
		'local/timer.c',
		'local/window.c',
		'local/actionbar.c',
		'local/bitmap.c',
		'local/draw.c',
		'local/hardwareOutput.c',
		'local/math.c',
		'local/animation.c'],
		includes=['include', 'SDL_gfx'],
		cflags=['-O2', '-Wall', '-std=c99'],
    	target='libPebbleLocalSim')

    # Resource compiler.
    bld.program(source=[
    	'resourceCompiler/main.c',
    	'resourceCompiler/jsmn.c'
    	],
		cflags=['-O2', '-Wall', '-std=c99'],
		lib=['SDL', 'SDL_image'],
    	target='resCompiler')
