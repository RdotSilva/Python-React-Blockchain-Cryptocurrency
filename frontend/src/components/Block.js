import React from "react";
import { MILLISECONDS_PY } from "../config";

function Block({ block }) {
  const { timestamp, hash, data } = block;
  const hashDisplay = `${hash.substring(0, 15)}...`;
  const timestampDisplay = new Date(
    timestamp / MILLISECONDS_PY
  ).toLocaleString();
}

export default Block;
