import React from 'react';
import { AppBar, Typography } from '@material-ui/core';
//import { CallMissedSharp } from '@material-ui/icons';
//Toolbar, IconButton, Badge, MenuItem, Menu, 

import useStyles from './styles';


const Navbar = () => {
    const classes = useStyles();
    return (
        <>
            <AppBar position="fixed" className={classes.appBar} color="inherit">
                <toolbar>
                    <Typography variant="h6" className={classes.title} color="inherit">
                        Japansk whiskey
                    </Typography>
                    <div className={classes.grow} />
                </toolbar>
            </AppBar>
        </>
    )
}

export default Navbar
