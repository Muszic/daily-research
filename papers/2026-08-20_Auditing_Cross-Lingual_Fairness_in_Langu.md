# Auditing Cross-Lingual Fairness in Language Model Watermarking

- **Category:** Cryptography
- **Date:** 2026-08-20
- **Link:** http://arxiv.org/abs/2608.20047v1

---
Here's a summary of the research paper in Markdown format:

## Auditing Cross-Lingual Fairness in Language Model Watermarking

### Problem

Current evaluations of large language model (LLM) text watermarking schemes are conducted almost exclusively on English text, using a narrow set of detection thresholds and quality measurements. This creates an untested and potentially flawed assumption that schemes performing well in English will generalize to other languages. Given that LLMs are deployed multilingually and misinformation is a significant cross-lingual threat, this English-centric evaluation overlooks critical cross-lingual fairness concerns and failure modes, where evaluation-design choices inconsequential in English become determinative cross-lingually.

### Method

The authors propose and apply a comprehensive evaluation framework designed for cross-lingual settings:

1.  **Empirically Calibrated Detection Thresholds:** Instead of theoretical defaults, thresholds are calibrated empirically per deployment context (per-language or global) to reflect actual false-positive rates.
2.  **Threshold-Independent Companion Measurement (AUC):** The Area Under the ROC Curve (AUC) is used alongside True Positive Rate (TPR) to distinguish *calibration failures* (high AUC, low TPR due to threshold issues) from true *detection failures* (low AUC and TPR).
3.  **Three Disjoint Quality Paradigms:** To capture different facets of generation quality preservation, the framework uses:
    *   **Distributional similarity (MAUVE):** Assesses aggregate distributional shift between watermarked and unwatermarked text.
    *   **Paired-semantic preservation (BERTScore):** Measures per-prompt semantic deviation.
    *   **Reference perplexity preservation (PPL-preservation):** Evaluates per-token likelihood preservation under an external reference LM.
4.  **Generalized-Entropy Decomposition (GE2):** Cross-language disparity in detection and quality scores is quantified using GE2, which is then decomposed into within-family and between-family components based on a pre-registered typological language partition (e.g., Germanic, Romance, Indic) to identify structural causes of disparity.

This framework was applied to an extensive experimental grid:
*   **Six watermarking schemes:** KGW, Unigram, XSIR (logit-bias family); DIP, SynthID-Text, EXPEdit (distortion-free family).
*   **Three open-weight generators:** Mistral-NeMo-12B, Gemma-3-4B, Qwen2.5-7B (in both base and instruction-tuned variants).
*   **Eleven languages:** Spanning four scripts (Latin, Devanagari, Arabic, Han+Kana) and eight typological families (Germanic, Romance, Turkic, Austroasiatic, Indic, Semitic, Sinitic, Japonic).
*   **Two generation regimes:** Base continuation (content-controlled FLORES+ prompts) and instruction-tuned (native-speaker AYA prompts).
The audit involved generating approximately 200,000 matched watermarked/unwatermarked outputs.

### Impact

The research reveals significant and previously uncharacterized cross-lingual fairness issues in LLM watermarking:

1.  **Detection and Calibration Failures:** The framework surfaces failure modes where watermarks are detectable (high AUC) but fail with default or global thresholds (low TPR) due to calibration issues (e.g., score distribution collapse). This highlights the necessity of per-language threshold calibration. Instruction-tuned models are shown to generally "collapse" detection across most schemes, often for calibrational reasons.
2.  **Quality Preservation Discrepancies:** "Distortion-free" watermarking schemes, despite their design goal, are empirically found to be the *most distorting* under the proposed quality metrics. Furthermore, per-scheme quality rankings vary significantly depending on the chosen quality measurement paradigm, underscoring the inadequacy of single-metric evaluations.
3.  **Structural Disparity:** The most critical finding is that observed cross-language disparity in both detection and quality is predominantly **between-family** on the typological partition (often accounting for over 90% of the generalized entropy). This indicates that fairness gaps in watermarking are **structural to language properties** (e.g., typology, script, tokenizer interactions) rather than idiosyncratic to specific languages. This implies that future watermarking research must adopt a typology-aware design and evaluation approach to ensure cross-lingual fairness.