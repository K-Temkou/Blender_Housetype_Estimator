import bpy
import random
from random import choice

i = 1

# here we are creating the first housetype that is going to make up the application while looping through the instances in order to order them in roughly 4x4 blocks
def glassfront():
    
    bpy.ops.object.select_all(action='SELECT')
    
    for obj in bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = obj
        bpy.context.object.hide_render = True
        obj.hide_set(True)
    
    i = 1
    
    while i <7:
    
        obj = bpy.context.scene.objects["glassfront"+str(1+i)]
    
        bpy.context.view_layer.objects.active = obj
        bpy.context.object.modifiers["Array"].count = random.randint(7,12)
    
        obj.location = (2, i*2, 0)
        i += 1
    
    
        if not obj.visible_get():
            obj.hide_set(False)
            obj.hide_viewport = False
            obj.select_set(True)
            bpy.context.object.hide_render = False
        
        
    i = 1

    while i <6:
    
        obj1 = bpy.context.scene.objects["glassfront"+str(1+i)+ ".001"]
    
        bpy.context.view_layer.objects.active = obj1
        bpy.context.object.modifiers["Array"].count = random.randint(7,12)
    
        obj1.location = (2+i*2, 2, 0)
        i= i+1
        
        if not obj1.visible_get():
            obj1.hide_set(False)
            obj1.hide_viewport = False
            obj1.select_set(True)
            bpy.context.object.hide_render = False
     
     
    i = 1
        
    while i <6:
    
        obj1 = bpy.context.scene.objects["glassfront"+str(1+i)+ ".001"]
    
        bpy.context.view_layer.objects.active = obj1
        bpy.context.object.modifiers["Array"].count = random.randint(7,12)
    
        obj1.location = (2+i*2, 2, 0)
        i= i+1
        
        if not obj1.visible_get():
            obj1.hide_set(False)
            obj1.hide_viewport = False
            obj1.select_set(True)
            bpy.context.object.hide_render = False
        
    i = 1
        
    while i <6:
    
        obj2 = bpy.context.scene.objects["glassfront"+str(1+i)+ ".002"]
    
        bpy.context.view_layer.objects.active = obj2
        bpy.context.object.modifiers["Array"].count = random.randint(7,12)
    
        obj2.location = (2+i*2, 12, 0)
        i= i+1
        
        if not obj2.visible_get():
            obj2.hide_set(False)
            obj2.hide_viewport = False
            obj2.select_set(True)
            bpy.context.object.hide_render = False
        
    i=1
        
    while i <5:
    
        obj3 = bpy.context.scene.objects["glassfront"+str(2+i)+ ".003"]
    
        bpy.context.view_layer.objects.active = obj3
        bpy.context.object.modifiers["Array"].count = random.randint(7,12)
    
        obj3.location = (12, 2 + i*2, 0)
        i += 1
        
        if not obj3.visible_get():
            obj3.hide_set(False)
            obj3.hide_viewport = False
            obj3.select_set(True)
            bpy.context.object.hide_render = False
            
        
    bpy.ops.object.select_all(action='DESELECT')
    
# for the next house type we are going for a different approach as we are creating the individual buildings first as they are made out of tree individual parts that are assembled together(roof, main, base)
# also it is important to enable or disable renderbility and visibility in the blender viewport depending if the object is part of the town or not
def dutch_building(j, i, k, n):
    
    hight = 0.7
        
    obj1 = bpy.context.scene.objects["base"+ str(j) +".00" +str(n)]
    obj = bpy.context.scene.objects["block"+ str(j) +".00" +str(n)]
    roof = bpy.context.scene.objects["roof"+ str(j) +".00" +str(n)]
    
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.modifiers["Array"].count = random.randint(3,4)
    count = bpy.context.object.modifiers["Array"].count +1.62
    
    bpy.context.object.hide_render = False
    
    bpy.context.view_layer.objects.active = obj1
    
    bpy.context.object.hide_render = False
    
    bpy.context.view_layer.objects.active = roof
    
    bpy.context.object.hide_render = False
    
    
    if not obj.visible_get():
        obj.hide_set(False)
        obj.hide_viewport = False
        obj.select_set(True)
            
    if not obj1.visible_get():
        obj1.hide_set(False)
        obj1.hide_viewport = False
        obj1.select_set(True)
            
    if not roof.visible_get():
        roof.hide_set(False)
        roof.hide_viewport = False
        roof.select_set(True)
        
    
    obj1.location = (k, i, 0)
    obj.location = (k, i, hight*2)
    roof.location =(k, i, hight*2*count)
    
        

#dutch_building()
# here we iterate trough the newly assembled buildings in order to sort them in the usual house_block format, this process is also repeated for our last building_type
def dutch_town():
    
    bpy.ops.object.select_all(action='SELECT')
    
    for obj in bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = obj
        bpy.context.object.hide_render = True
        obj.hide_set(True)
    

    j = 1
    while j< 7:
        
        dutch_building(j,j*2, 2, 1)
        j += 1
        
     
    j = 1
    
    while j< 7:
        dutch_building(j,j*2, 12, 2)
        j += 1
        
    
    j = 1
    while j< 5:
        dutch_building(j, 2, 2+j*2, 3)
        j += 1
        
    j = 1
        
    while j< 5:
        dutch_building(j, 12, 2+j*2, 4)
        j += 1
        
        
    bpy.ops.object.select_all(action='DESELECT')
        

def highriseBuilding(j, i, k, n):
    
    hight = 0.65
        
    obj1 = bpy.context.scene.objects["old_base"+ str(j) +".00" +str(n)]
    obj = bpy.context.scene.objects["old_block"+ str(j) +".00" +str(n)]
    roof = bpy.context.scene.objects["old_roof"+ str(j) +".00" +str(n)]
    
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.modifiers["Array"].count = random.randint(6,9)
    count = bpy.context.object.modifiers["Array"].count +1.62
    
    bpy.context.object.hide_render = False
    
    bpy.context.view_layer.objects.active = obj1
    
    bpy.context.object.hide_render = False
    
    bpy.context.view_layer.objects.active = roof
    
    bpy.context.object.hide_render = False
    
    
    
    if not obj.visible_get():
        obj.hide_set(False)
        obj.hide_viewport = False
        obj.select_set(True)
            
    if not obj1.visible_get():
        obj1.hide_set(False)
        obj1.hide_viewport = False
        obj1.select_set(True)
            
    if not roof.visible_get():
        roof.hide_set(False)
        roof.hide_viewport = False
        roof.select_set(True)
        
    
    obj1.location = (k, i, 0)
    obj.location = (k, i, hight*2)
    roof.location =(k, i, hight*count-0.4)
    
        
def highrise_town():
    
    bpy.ops.object.select_all(action='SELECT')

    for obj in bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = obj
        bpy.context.object.hide_render = True
        obj.hide_set(True)
    
    j = 1
    while j< 7:
        
        highriseBuilding(j,j*2, 2, 1)
        j += 1
        
     
    j = 1
    
    while j< 7:
        highriseBuilding(j,j*2, 12, 2)
        j += 1
        
    
    j = 1
    while j< 5:
        highriseBuilding(j, 2, 2+j*2, 3)
        j += 1
        
    j = 1
        
    while j< 5:
        highriseBuilding(j, 12, 2+j*2, 4)
        j += 1

    bpy.ops.object.select_all(action='DESELECT')
        
#dutch_town()
        
#highrise_town()

#glassfront()

def estimate():
   
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.render.image_settings.file_format="PNG"
    path = r"C:\Users\Have Fun\Documents\renders/render"
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(use_viewport=True, write_still=True)
    

#estimate()

# here we add renders of our test_subject to a custom training dataset in order to enhance the future models accurarcy while predicting those
def create_train_dataset():
   
   for i in range(30):
       highrise_town()
       
       bpy.context.scene.render.engine = 'BLENDER_EEVEE'
       bpy.context.scene.render.image_settings.file_format="PNG"
       path = r"C:\Users\Have Fun\Documents\renders/highrise_town" + str(i)
       bpy.context.scene.render.filepath = path
       bpy.ops.render.render(use_viewport=True, write_still=True)
    
        
#train()
#highrise_town()
def random_building_scatterer():
    
   # yet to be defined
