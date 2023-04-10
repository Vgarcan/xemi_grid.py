from turtle import Turtle


class Grid:
  '''Call draw_grid() to start drawing. Call cell_color="str" or axis_color="str" to change the colors of the CELLS and the AXIS'''

  def __init__(self):

    self.tim = Turtle()
    self.tim.ht()
    self.tim.penup()
    self.tim.speed(10)
    self.cell_color = 'black'
    self.axis_color = 'red'

  def draw_grid(self, height, width, value, axis_on=False):
    '''Draw a Grid with the given arguments HEIGHT and WIDTH. VALUE refers to the size of the square. If AXIS_ON = True will draw positions 0 besides the size of the square'''
   
    ### DRAW GRID ###
    self.xpos = -1 * (height / 2)
    self.ypos = width / 2
    self.tim.pencolor(self.cell_color)
    self.tim.setposition(self.xpos, self.ypos)

    ## Drawing loop ##
    drawing = True
    while drawing:
      self.tim.pendown()

      ## Draw Y ##
      self.tim.goto(self.xpos, -1 * self.ypos)
      self.xpos += value
      if self.xpos > height / 2:
        self.tim.penup()
        self.xpos = -1 * (height / 2)
        self.ypos = width / 2
        self.tim.goto(self.xpos, self.ypos)
        while drawing:
          self.tim.pendown()

          ## Draw X ##
          self.tim.goto(-1 * self.xpos, self.ypos)
          self.ypos -= value
          self.tim.penup()
          self.tim.goto(self.xpos, self.ypos)
          if self.ypos < -1 * (width / 2):
            self.tim.penup()
            self.xpos = -1 * (height / 2)
            self.ypos = width / 2
            self.tim.goto(self.xpos, self.ypos)
            drawing = False
      
      ## Go to TOP LEFT ##
      self.tim.penup()
      self.tim.goto(self.xpos, self.ypos)

     ## AXIS_ON ##
    if axis_on == True:
      self.tim.pencolor(self.axis_color)
      ### DRAW AXIS Y ###
      self.tim.pu()
      self.tim.goto(height / 2, 0)
      self.tim.pd()
      self.tim.goto(-1 * (height / 2), 0)
      ### DRAW AXIS X ###
      self.tim.pu()
      self.tim.goto(0, width / 2)
      self.tim.pd()
      self.tim.goto(0, -1 * (width / 2))
      self.tim.pu()