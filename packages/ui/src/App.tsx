import "./App.css";
import "@copilotkit/react-ui/styles.css";
import { CopilotKitPage } from "./components/CopilotKitPage";
import { CopilotKit } from "@copilotkit/react-core";

function App() {
  return (
    <>
      <CopilotKit runtimeUrl="/api/copilotkit" agent="strands_agent">
        <CopilotKitPage />
      </CopilotKit>
    </>
  );
}

export default App;
