const {
    colors,
    CssBaseline,
    ThemeProvider,
    Container,
    createTheme,
    Button
} = MaterialUI;




const theme = createTheme({
    palette: {
        primary: {
            main: '#556cd6',
        },
        secondary: {
            main: '#19857b',
        },
        error: {
            main: colors.red.A400,
        },
        background: {
            default: '#fff',
        },
    },
});


function App() {
    return (
        <Container>
            <Button>Hi</Button>
        </Container>
    );
}

ReactDOM.render(
    <ThemeProvider theme={theme}>
        <CssBaseline/>
        <App/>
    </ThemeProvider>,
    document.querySelector('#root'),
);