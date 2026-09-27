---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: Exchange traded futures date and time dependent terms such as prices and margining. Also covers greeks (thetas
      etc.)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Futures Temporal Ontology
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2023 EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - concept: /concepts/fibo/MD/DerivativesTemporal/FuturesTemporal.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/
sources:
- id: fibo-source-c2e233cb71
  resource: references/fibo/MD/DerivativesTemporal/FuturesTemporal.rdf
  sha256: c2e233cb71a6057762c1da19bf2b1316166cd651fcf570e55af51b91c70f41c5
  title: FIBO source MD/DerivativesTemporal/FuturesTemporal.rdf
title: Futures Temporal Ontology
type: Ontology Definition
---

# Futures Temporal Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/>

## Relationships

- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [FuturesTemporal](/concepts/fibo/MD/DerivativesTemporal/FuturesTemporal.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: Exchange traded futures date and time dependent terms such as prices and margining. Also covers greeks (thetas etc.)
- **license**: https://opensource.org/licenses/MIT
- **label** (en): Futures Temporal Ontology
- **copyright**: Copyright (c) 2013-2023 EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
