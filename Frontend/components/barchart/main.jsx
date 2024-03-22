const BarChart = ({ data }) => {
    return (
        <div>
            <Bar
                data={data}
                options={{
                    plugins: {
                        title: {
                            display: true,
                            text: 'Bar Chart Example'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }}
            />
        </div>
    );
};

export default BarChart;