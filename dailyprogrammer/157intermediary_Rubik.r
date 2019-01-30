rubik <- function(moves) {

    cube <- list('U'=matrix('y', 3, 3),
        'D'=matrix('w', 3, 3),
        'F'=matrix('r', 3, 3),
        'R'=matrix('g', 3, 3),
        'B'=matrix('o', 3, 3),
        'L'=matrix('b', 3, 3)
    );

    moves <- unlist(strsplit(moves, '\\s'));
    for (i in 1:length(moves)) {
        cube <- rotatecube(cube, substr(moves[i],1,1));

        if (substr(moves[i],2,2) == '2') {
            cube <- rotatecube(cube, substr(moves[i],1,1));
        } else if (substr(moves[i],2,2) == '\'') {
            cube <- rotatecube(cube, substr(moves[i],1,1));
            cube <- rotatecube(cube, substr(moves[i],1,1));
        }
    }

    write.table(cube[['F']],row.names=F,col.names=F,sep="",quote=FALSE)
}

rotatecube <- function(cube, move) {
    cube[[move]] <- rot90(cube[[move]]);
    if (move == 'U') {
        tmp <- cube[['F']];
        cube[['F']][1,] <- cube[['R']][1,];
        cube[['R']][1,] <- cube[['B']][1,];
        cube[['B']][1,] <- cube[['L']][1,];
        cube[['L']][1,] <- tmp[1,];
    } else if (move == 'D') {
        tmp <- cube[['L']]
        cube[['L']][3,] <- cube[['B']][3,];
        cube[['B']][3,] <- cube[['R']][3,];
        cube[['R']][3,] <- cube[['F']][3,];
        cube[['F']][3,] <- tmp[3,];
    } else if (move == 'F') {
        tmp <- cube[['D']]
        cube[['D']][1,] <- rev(cube[['R']][,1]);
        cube[['R']][,1] <- cube[['U']][3,];
        cube[['U']][3,] <- rev(cube[['L']][,3]);
        cube[['L']][,3] <- tmp[1,];
    } else if (move == 'B') {
        tmp <- cube[['L']]
        cube[['L']][,1] <- rev(cube[['U']][1,]);
        cube[['U']][1,] <- cube[['R']][,3];
        cube[['R']][,3] <- rev(cube[['D']][3,]);
        cube[['D']][3,] <- tmp[,1];
    } else if (move == 'R') {
        tmp <- cube[['D']]
        cube[['D']][,3] <- rev(cube[['B']][,1]);
        cube[['B']][,1] <- rev(cube[['U']][,3]);
        cube[['U']][,3] <- cube[['F']][,3];
        cube[['F']][,3] <- tmp[,3];
    } else if (move == 'L') {
        tmp <- cube[['D']]
        cube[['D']][,1] <- cube[['F']][,1];
        cube[['F']][,1] <- cube[['U']][,1];
        cube[['U']][,1] <- rev(cube[['B']][,3]);
        cube[['B']][,3] <- rev(tmp[,1]);
    }

    return (cube);
}

rot90 <- function(mat) {
    t(mat[nrow(mat):1,,drop=FALSE])
}
