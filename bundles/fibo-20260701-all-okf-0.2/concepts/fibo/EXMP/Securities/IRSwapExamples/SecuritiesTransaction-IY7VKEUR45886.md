---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities transaction IY7VKEUR45886
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities transaction for contract IY7VKEUR45886
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Need to create the trade event - this is the activity (maybe we should rename these now? in FND to activity and
      event?) and add lifecycle elements - date and time, status of the trade and settlement status
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/IRSwapExamples/Contract-IY7VKEUR45886.md
    predicate: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/Contract-IY7VKEUR45886
  - concept: /concepts/fibo/EXMP/Securities/IRSwapExamples/Trader-J_Adams.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isFacilitatedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/Trader-J_Adams
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/SecuritiesTransaction-IY7VKEUR45886
sources:
- id: fibo-source-dbb6868e12
  resource: references/fibo/EXMP/Securities/IRSwapExamples.rdf
  sha256: dbb6868e124bba0f62a80f6387c9e212e8d2931ed572f2e411e31534e2edcfc5
  title: FIBO source EXMP/Securities/IRSwapExamples.rdf
title: securities transaction IY7VKEUR45886
type: Ontology Individual
---

# securities transaction IY7VKEUR45886

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/SecuritiesTransaction-IY7VKEUR45886>

## Definition

securities transaction for contract IY7VKEUR45886

## Relationships

- **Related to**: [Trader-J_Adams](/concepts/fibo/EXMP/Securities/IRSwapExamples/Trader-J_Adams.md)
- **Related to**: [Contract-IY7VKEUR45886](/concepts/fibo/EXMP/Securities/IRSwapExamples/Contract-IY7VKEUR45886.md)

## Annotations

- **label**: securities transaction IY7VKEUR45886
- **definition**: securities transaction for contract IY7VKEUR45886
- **explanatoryNote**: Need to create the trade event - this is the activity (maybe we should rename these now? in FND to activity and event?) and add lifecycle elements - date and time, status of the trade and settlement status

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
