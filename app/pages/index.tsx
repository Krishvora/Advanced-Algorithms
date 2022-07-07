import type { NextPage } from "next";
import styles from "../styles/Home.module.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Console from "../components/Console";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Median Finding Algorithm</h1>

      <Console />
      <section className={styles.footer}>
        <p className={styles.description}>
          CS 601 Team 4 - Yeh-Tarn Su, Krish Vora
        </p>
      </section>
    </div>
  );
};

export default Home;
