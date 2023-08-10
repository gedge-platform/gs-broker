import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { useLocation } from "react-router-dom";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import { styled } from "@mui/system";

import DashboardLayout from "components/LayoutContainers/DashboardLayout";
import Message from "layouts/management/components/message";
import axiosInstance from "axiosInstance";

function Management() {

  return (
    <DashboardLayout>
      <Box pt={2} sx={{ width: "100%" }}>
        <Message clusterId={cluster.id} />
      </Box>
    </DashboardLayout>
  );
}

export default Management;
