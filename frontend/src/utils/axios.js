import axios from "axios";

const BASE_URL = "http://localhost:8000";

const axiosInst = axios.create({baseURL: BASE_URL})

axiosInst.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(
        (error.response && error.response.data) || "Something went wrong"
    )
)

export default axiosInst;