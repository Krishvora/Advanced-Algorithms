import type { NextPage } from "next";
import styles from "../styles/Home.module.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Console from "../components/Console";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Median Finding Algorithm</h1>

      <Console />
    </div>
  );
};

export default Home;
