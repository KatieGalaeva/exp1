from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


class RectangleInput(BaseModel):
    """
    Input coords
    """
    x: float  
    y: float  
    w: float  
    h: float 

class RectangleOutput(BaseModel):
    """
    Output coords
    """
    x: float  
    y: float 
    w: float 
    h: float  

app = FastAPI(
    title="Intersection Service",
    description="Service for calculation of intersection rectangles",
    version="1.0"
)

def intersect_rectangles(rect_b: RectangleInput):
    # Defaukt value of rect_a
    a_x, a_y, a_w, a_h = 0, 0, 1000, 500

    # Find coords of top right corner rect_a
    a_right = a_x + a_w
    a_top = a_y + a_h

    # Find coords of top right corner rect_b
    b_right = rect_b.x + rect_b.w
    b_top = rect_b.y + rect_b.h

    # Calculate intersection boundaries
    inter_left = max(a_x, rect_b.x)
    inter_bottom = max(a_y, rect_b.y)
    inter_right = min(a_right, b_right)
    inter_top = min(a_top, b_top)

    # Check for intersection
    if inter_right <= inter_left or inter_top <= inter_bottom:
        return None

    return RectangleOutput(
        x = inter_left,
        y = inter_bottom,
        w = inter_right - inter_left,
        h = inter_top - inter_bottom
    )


@app.post("/intersect", response_model=Optional[RectangleOutput])
async def get_intersection(rectangle: RectangleInput):
    """
    Input coords of rect_b
    Return the coords of intersection if possible else None
    """
    result = intersect_rectangles(rectangle)
    return result
