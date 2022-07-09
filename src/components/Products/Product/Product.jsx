  
import React from 'react';
import { Card, CardMedia, CardContent, Typography, CardActionArea } from '@material-ui/core';

import useStyles from './styles';

var baseurl = "https://www.vinmonopolet.no/"
const Product = ({ product }) => {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea target="_blank" href={baseurl + product.url} >
        <CardMedia className={classes.media} image={product.images} title={product.name} />
        <CardContent>
          <div className={classes.cardContent}>
            <Typography gutterBottom variant="h6" component="h2">
              {product.name}
            </Typography>
            <Typography gutterBottom variant="h5" component="h2">
              {product.price}
            </Typography>
          </div>
          <Typography dangerouslySetInnerHTML={{ __html: product.product_selection }} variant="body2" color="textSecondary" component="p" />
        </CardContent>
      </CardActionArea>
    </Card>
  );
};

export default Product;
