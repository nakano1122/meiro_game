export interface EmptyMaze {
    isWall: boolean;
    hasPlayer: boolean;
    isStart: boolean;
    isGoal: boolean;
    isOnePoint: boolean;
    isTwoPoint: boolean;
    isThreePoint: boolean;
    isFourPoint: boolean;
    isFivePoint: boolean;
}

export interface MazeData {
    id: number;
    level: string;
    stepLimit: number;
    grid: EmptyMaze[][];
}