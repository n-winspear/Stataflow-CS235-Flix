import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import TempMovieImage from "components/home/images/TempMovieImage.jpg";

const useStyles = makeStyles({
  root: {
    maxWidth: 336,
  },
  media: {
    height: 189,
  },
});

export default function MediaCard({ movieData }) {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          title={movieData.title}
          image={TempMovieImage}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {movieData.title}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {movieData.description}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Rate
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>
    </Card>
  );
}
