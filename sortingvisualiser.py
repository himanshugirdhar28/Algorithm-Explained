import pygame
import random
import math
from queue import Queue
pygame.init()

class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE
    GRADIENTS =[(128,128,128),(160,160,160),(192,192,192)]

    FONT=pygame.font.SysFont('verdana',22)
    SMALL_FONT=pygame.font.SysFont('verdana',18)
    LARGE_FONT = pygame.font.SysFont('verdana',32,bold=True)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self,width,height,lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualisation")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst=lst
        self.min_val=min(lst)
        self.max_val=max(lst)

        self.block_width= round((self.width-self.SIDE_PAD)/len(lst))
        self.block_height=math.floor((self.height-self.TOP_PAD)/(self.max_val-self.min_val))
        self.start_x=self.SIDE_PAD//2

def draw(draw_info, algo_name, ascending,popupmenu,image):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    

    # pygame.draw.rect(draw_info.window, (138,137,136) ,(0,0,1366,150)) #(46,64,82)
    image_back = pygame.image.load(r'S:\\program\\visualisation project\\back5.jpg')
    image_back  = pygame.transform.smoothscale(image_back, (1366,766))
    draw_info.window.blit(image_back, (0, 0))

    pygame.draw.rect(draw_info.window, draw_info.WHITE, (350, 0, 4 , 152))

    pygame.draw.rect(draw_info.window, draw_info.WHITE, (1010, 5, 4 , 140))
    global b6
    b6=pygame.draw.circle(draw_info.window,draw_info.WHITE,(1012,y_pos),8)

    pygame.draw.rect(draw_info.window, draw_info.WHITE, (1230, 5, 4 , 140))
    global b7
    b7=pygame.draw.circle(draw_info.window,draw_info.WHITE,(1232,y_pos1),8)

    # title1 =draw_info.LARGE_FONT.render(algo_name,1,(178,97,199))
    # draw_info.window.blit(title1, (draw_info.width/2-title1.get_width()/2,5))

    title =draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}",1,(draw_info.WHITE))
    draw_info.window.blit(title, (draw_info.width/2-title.get_width()/2,35))

    controls=draw_info.SMALL_FONT.render("R - reset | SPACE - Start/Stop Sorting | A - Ascending | D- Descending", 1, draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 ,draw_info.TOP_PAD-40)) #

    global ba1
    global ba2
    global ba3
    global ba4
    global ba5

    algorithm1=draw_info.SMALL_FONT.render("Insertion Sort", 1,algo_color1)
    ba1=draw_info.window.blit(algorithm1, (20, 40)) 
    (_,_,wa,_)=algorithm1.get_rect()


    algorithm2=draw_info.SMALL_FONT.render("Bubble Sort", 1, algo_color2)
    ba2=draw_info.window.blit(algorithm2, (20+wa+40, 40)) 

    algorithm3=draw_info.SMALL_FONT.render("Selection Sort", 1, algo_color3)
    ba3=draw_info.window.blit(algorithm3, (20, 70)) 

    algorithm4=draw_info.SMALL_FONT.render("Quick Sort", 1, algo_color4)
    ba4=draw_info.window.blit(algorithm4, (20+wa+40, 70)) 

    # algorithm5=draw_info.SMALL_FONT.render("Merge Sort", 1, algo_color5)
    # ba5=draw_info.window.blit(algorithm5, (20, 100)) 


    (image,image1,image2,image3,image4,image5)=image
    global im1
    im1=draw_info.window.blit(image, (1100, 55))
    global im2
    im2=draw_info.window.blit(image1, (1100, 105))
    global im3
    im3=draw_info.window.blit(image2, (1100, 5))
    global im4
    im4=draw_info.window.blit(image3, (1100-50, 55))
    global im5
    im5=draw_info.window.blit(image4, (1100+50, 55))
    global im6
    im6=draw_info.window.blit(image5, (1100+180, 50))


    popup =draw_info.FONT.render("Sorting Algorithms",1,(252,251,250) )
    global b1
    a=50
    b=2
    c=30
    ncolor=draw_info.BLACK
    x,y,w,h = popup.get_rect()
    h+=5
    x, y = a,b
    # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y), (x + w , y), 5)
    # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    # pygame.draw.line(draw_info.window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(draw_info.window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(draw_info.window, ncolor, (x-10, y, w+20 , h))
    b1=draw_info.window.blit(popup, (a,b))
    global b2
    global b3
    global b4
    global b5

    if popupmenu:
        popup2 =draw_info.FONT.render("Insertion Sort",1,(252,251,250) )
        x,y,w,h = popup.get_rect()
        x, y = a,b+c
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y), (x + w , y), 5)
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        # pygame.draw.line(draw_info.window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(draw_info.window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(draw_info.window, ncolor, (x-10, y, w+20 , h+5))
        b2=draw_info.window.blit(popup2, (50,b+c))

        popup3 =draw_info.FONT.render("Bubble Sort",1,draw_info.WHITE)
        x,y,w,h = popup.get_rect()
        x, y = 50,b+c*2
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y), (x + w , y), 5)
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        # pygame.draw.line(draw_info.window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(draw_info.window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(draw_info.window, ncolor, (x-10, y, w+20 , h+5))
        b3=draw_info.window.blit(popup3, (50,b+c*2))

        popup4 =draw_info.FONT.render("Selection Sort",1,draw_info.WHITE)
        x,y,w,h = popup.get_rect()
        x, y = 50,b+c*3
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y), (x + w , y), 5)
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        # pygame.draw.line(draw_info.window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(draw_info.window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(draw_info.window, ncolor, (x-10, y, w+20 , h+5))
        b4=draw_info.window.blit(popup4, (50,b+c*3))

        popup5 =draw_info.FONT.render("Quick Sort",1,draw_info.WHITE)
        x,y,w,h = popup.get_rect()
        x, y = 50,b+ c*4
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y), (x + w , y), 5)
        # pygame.draw.line(draw_info.window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        # pygame.draw.line(draw_info.window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(draw_info.window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(draw_info.window, ncolor, (x-10, y, w+20 , h+5))
        b5=draw_info.window.blit(popup5, (50,b+c*4))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={},clear_bg=False):
    lst=draw_info.lst

    if clear_bg:
        clear_rect=(0, draw_info.TOP_PAD, draw_info.width, draw_info.height-draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR,clear_rect)
        draw(draw_info, sorting_algo_name, ascending,popupmenu,image)
        
    for i,val in enumerate(lst):
        x=draw_info.start_x+i*draw_info.block_width
        y=draw_info.height-(val-draw_info.min_val)*draw_info.block_height
        # print("y is :",y)

        color=draw_info.GRADIENTS[i%3]

        if i in color_positions:
            color=color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x,y, draw_info.block_width,(val-draw_info.min_val)*draw_info.block_height),0,0,200//len(draw_info.lst),200//len(draw_info.lst),)
    
    if clear_bg:
        pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    lst=[]

    for _ in range(n):
        val=random.randint(min_val, max_val)
        # print(val)
        lst.append(val)

    return lst

def bubble_sort(draw_info, ascending=True):
    lst= draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1=lst[j]
            num2=lst[j+1]

            if(num1>num2 and ascending) or (num1<num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1],lst[j]
                draw_list(draw_info, {j:draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst=draw_info.lst

    for i in range(1,len(lst)):
        current=lst[i]

        while True:
            ascending_sort = i>0 and lst[i-1]>current and ascending
            descending_sort= i>0 and lst[i-1]<current and not ascending

            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i-1]
            i=i-1
            lst[i]= current
            draw_list(draw_info, {i-1: draw_info.GREEN, i:draw_info.RED}, True)
            yield True

    return lst
def selection_sort(draw_info, ascending=True):
    lst=draw_info.lst
    for i in range(0,len(lst)-1):
        count=lst[i]
        k=i
        for j in range(i,len(lst)):
            if((lst[j]<count and ascending) or (lst[j]>count and not ascending)):
                count=lst[j]
                k=j
            draw_list(draw_info, {j:draw_info.GREEN, k: draw_info.RED}, True)
            yield True
        draw_list(draw_info, {i:draw_info.GREEN, k:draw_info.RED}, True)
        yield True
        (lst[k],lst[i])=(lst[i],lst[k])
        draw_list(draw_info, {i:draw_info.RED, k: draw_info.GREEN}, True)
        yield True
    return(lst)
# def quick_sortr(draw_info,lst,s,f,ascending=True,):
#     if(f-s<=1):
#         return
#     i=s
#     j=s
#     while(j<f):
#         if(lst[j]<=lst[s]):
#             lst[j],lst[i]=lst[i],lst[j]
#             i+=1
#             j+=1
#         elif(lst[j]>lst[s]):
#             j+=1
#         draw_list(draw_info, {j:draw_info.GREEN, i: draw_info.RED}, True)
#         yield True
#     lst[i-1],lst[s]=lst[s],lst[i-1]
#     quick_sortr(draw_info,lst,s,i-1,ascending)
#     quick_sortr(draw_info,lst,i,f,ascending)
#     return
def quick_sort(draw_info,ascending=True):
    lst=draw_info.lst
    q=Queue()
    q.put([0,len(lst)])
    while(not q.empty()):
        # if(f-s<=1):
        #     return
        i=q.queue[0][0]
        j=q.queue[0][0]
        while(j<q.queue[0][1]):
            if(lst[j]<=lst[q.queue[0][0]]):
                lst[j],lst[i]=lst[i],lst[j]
                i+=1
                j+=1
            elif(lst[j]>lst[q.queue[0][0]]):
                j+=1
            draw_list(draw_info, {j:draw_info.GREEN, i: draw_info.RED}, True)
            yield True
        lst[i-1],lst[q.queue[0][0]]=lst[q.queue[0][0]],lst[i-1]
        if(i-1-q.queue[0][0]>1):
            q.put([q.queue[0][0],i-1])
        if(q.queue[0][1]-i>1):
            q.put([i,q.queue[0][1]])
        q.get()
        # quick_sortr(lst,s,i-1)
        # quick_sortr(lst,i,f)
        # return
    return(lst)
# def heap_rectify(draw_info,lst,s,f):
#     i=s
#     while(2*i+1<f):
#         if(2*i+2<f):
#             if(lst[i]<max(lst[2*i+1],lst[2*i+2])):
#                 if(lst[2*i+1]>lst[2*i+2]):
#                     lst[i],lst[2*i+1]=lst[2*i+1],lst[i]
#                     i=2*i+1
#                 else:
#                     lst[i],lst[2*i+2]=lst[2*i+2],lst[i]
#                     i=2*i+2
#             else:
#                     break
#         else:
#             if(lst[i]<lst[2*i+1]):
#                 lst[i],lst[2*i+1]=lst[2*i+1],lst[i]
#                 i=2*i+1
#             else:
#                 break
#         draw_list(draw_info, {(i-1)//2:draw_info.GREEN, i: draw_info.RED}, True)
#         yield True
# def heapify(lst):
#     i=(len(lst)-1)//2
#     while(i>=0):
#         heap_rectify(lst,i,len(lst))
#         # j=i
#         # while(2*j+1<len(lst)):
#         #     if(2*j+2<len(lst)):
#         #         if(lst[j]<max(lst[2*j+1],lst[2*j+2])):
#         #             if(lst[2*j+1]>lst[2*j+2]):
#         #                 lst[j],lst[2*j+1]=lst[2*j+1],lst[j]
#         #                 j=2*j+1
#         #             else:
#         #                 lst[j],lst[2*j+2]=lst[2*j+2],lst[j]
#         #                 j=2*j+2
#         #         else:
#         #             break
#         #     else:
#         #         if(lst[j]<lst[2*j+1]):
#         #             lst[j],lst[2*j+1]=lst[2*j+1],lst[j]
#         #             j=2*j+1
#         #         else:
#         #             break
#         i-=1
# def heap_sort(draw_info,ascending=True):
#     lst=draw_info.lst
#     heapify(lst)
#     i=0
#     print(lst)
#     while i<(len(lst)):
#         lst[0],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[0]
#         heap_rectify(draw_info,lst,0,len(lst)-i-1)
#         i+=1
#     return(lst)
def main():
    run=True
    clock=pygame.time.Clock()
    count=0
    n=80
    min_val=10
    max_val=100

    lst=generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1366,768,lst)
    global ascending
    global sorting
    global sorting_algorithm
    global sorting_algo_name
    global popupmenu
    global image
    global algo_color1
    global algo_color2
    global algo_color3
    global algo_color4
    global algo_color5
    (algo_color1,algo_color2,algo_color3,algo_color4,algo_color5) =(draw_info.WHITE,draw_info.BLACK,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
    sorting = False
    ascending = True
    play=True
    drag=True
    global y_pos
    global y_pos1
    y_pos=75
    y_pos1=75
    speed = 5
    img_size=38

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator= None
    popupmenu=False
    image = pygame.image.load(r'S:\\program\\visualisation project\\p1.png')
    image1 = pygame.image.load(r'S:\\program\\visualisation project\\p2.png')
    image2 = pygame.image.load(r'S:\\program\\visualisation project\\p3.png')
    image3 = pygame.image.load(r'S:\\program\\visualisation project\\p4.png')
    image4 = pygame.image.load(r'S:\\program\\visualisation project\\p5.png')
    image5 = pygame.image.load(r'S:\\program\\visualisation project\\p6.png')
    image  = pygame.transform.smoothscale(image, (img_size,img_size))
    image1 = pygame.transform.smoothscale(image1, (img_size,img_size))
    image2 = pygame.transform.smoothscale(image2, (img_size,img_size))
    image3 = pygame.transform.smoothscale(image3, (img_size,img_size))
    image4 = pygame.transform.smoothscale(image4, (img_size,img_size))
    image5 = pygame.transform.smoothscale(image5, (50,50))
    image=(image,image1,image2,image3,image4,image5)
    draw(draw_info, sorting_algo_name, ascending,popupmenu,image)
    while run:
        clock.tick(speed)
        if sorting and play:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting =False
        elif play:
            draw(draw_info, sorting_algo_name, ascending,popupmenu,image)
        
        if drag:
            # print(pygame.mouse.get_pressed)
            if pygame.mouse.get_pressed(num_buttons=3)==(True, False,False):
                if(pygame.mouse.get_pos()[0]>970 and pygame.mouse.get_pos()[0]<1050 and pygame.mouse.get_pos()[1]>0 and pygame.mouse.get_pos()[1]<150):
                    (_,y_pos)=pygame.mouse.get_pos()
                    speed=150-y_pos
                    draw(draw_info, sorting_algo_name, ascending,popupmenu,image)
                elif(pygame.mouse.get_pos()[0]>1200 and pygame.mouse.get_pos()[0]<1260 and pygame.mouse.get_pos()[1]>0 and pygame.mouse.get_pos()[1]<150):
                    (_,y_pos1)=pygame.mouse.get_pos()
                    n=165-y_pos1
                    lst=generate_starting_list(n, min_val, max_val)
                    draw_info = DrawInformation(1366,768,lst)
                    draw(draw_info, sorting_algo_name, ascending,popupmenu,image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            if event.type  == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    if(not count%2):
                        popupmenu=True
                    else:
                        popupmenu=False
                    count+=1
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                # elif b6.collidepoint(pygame.mouse.get_pos()) or b7.collidepoint(pygame.mouse.get_pos()):
                #     drag=True
                #     draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                elif ba1.collidepoint(pygame.mouse.get_pos()):
                    (algo_color2,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color1=draw_info.BLACK
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif ba2.collidepoint(pygame.mouse.get_pos()):
                    (algo_color1,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color2=draw_info.BLACK
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif ba3.collidepoint(pygame.mouse.get_pos()):
                    (algo_color1,algo_color2,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color3=draw_info.BLACK
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif ba4.collidepoint(pygame.mouse.get_pos()):
                    (algo_color1,algo_color2,algo_color3,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color4=draw_info.BLACK
                    sorting_algorithm = quick_sort
                    sorting_algo_name = "Quick Sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
                # elif ba5.collidepoint(pygame.mouse.get_pos()):
                #     (algo_color1,algo_color2,algo_color3,algo_color4)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                #     algo_color5=draw_info.BLACK
                #     sorting_algorithm = heap_sort
                #     sorting_algo_name = "Heap Sort"
                #     draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                #     sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
                elif popupmenu and b2.collidepoint(pygame.mouse.get_pos()):
                    (algo_color2,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color1=draw_info.BLACK
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                    popupmenu=False
                    count=0
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif popupmenu and b3.collidepoint(pygame.mouse.get_pos()):
                    (algo_color1,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color2=draw_info.BLACK
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                    popupmenu=False
                    count=0
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif popupmenu and b4.collidepoint(pygame.mouse.get_pos()):
                    (algo_color1,algo_color2,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color3=draw_info.BLACK
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                    popupmenu=False
                    count=0
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif popupmenu and b5.collidepoint(pygame.mouse.get_pos()):
                    popupmenu=False
                    count=0
                elif im1.collidepoint(pygame.mouse.get_pos()):
                    popupmenu=False
                    count=0
                    sorting = True
                    play = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif im2.collidepoint(pygame.mouse.get_pos()):
                    play= False
                elif im3.collidepoint(pygame.mouse.get_pos()):
                    lst=generate_starting_list(n,min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                    play=True
                elif im5.collidepoint(pygame.mouse.get_pos()):
                    if sorting and not play:
                        try:
                            next(sorting_algorithm_generator)
                        except StopIteration:
                            sorting =False
                elif im6.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    lst=generate_starting_list(n,min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key== pygame.K_RIGHT:
                    if sorting and not play:
                        try:
                            next(sorting_algorithm_generator)
                        except StopIteration:
                            sorting =False
                elif event.key== pygame.K_SPACE:
                    if not play:
                        play=True
                        continue
                    if sorting:
                        play=False
                        continue
                    popupmenu=False
                    count=0
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_i:
                    (algo_color2,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color1=draw_info.BLACK
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_b:
                    (algo_color1,algo_color3,algo_color4,algo_color5)=(draw_info.WHITE,draw_info.WHITE,draw_info.WHITE,draw_info.WHITE)
                    algo_color2=draw_info.BLACK
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble_sort"
                    draw(draw_info, sorting_algo_name, ascending,popupmenu, image)
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
    pygame.quit()

def hello():
    print("hello")
if __name__ == "__main__":
    main()






