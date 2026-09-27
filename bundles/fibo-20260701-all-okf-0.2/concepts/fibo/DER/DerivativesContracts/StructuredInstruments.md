---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts common to pre-packaged structured finance investment strategies based on a host
      of underlying instruments, pools, or other assets.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: http://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Structured Instruments Ontology
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2023 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/20230401/DerivativesContracts/StructuredInstruments/
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: Structured Instruments Ontology
type: Ontology Definition
---

# Structured Instruments Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/>

## Relationships

- **Related to**: [DerivativesBasics](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md)
- **Related to**: [SecurityBasedDerivatives](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [PoolBackedSecurities](/concepts/fibo/SEC/Debt/PoolBackedSecurities.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [StructuredInstruments](<https://spec.edmcouncil.org/fibo/ontology/DER/20230401/DerivativesContracts/StructuredInstruments/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts common to pre-packaged structured finance investment strategies based on a host of underlying instruments, pools, or other assets.
- **license**: http://opensource.org/licenses/MIT
- **label** (en): Structured Instruments Ontology
- **copyright**: Copyright (c) 2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2023 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
