---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund distribution policy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: policy indicating the overall strategy or limitations on distribution for the fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Note that individual classes of Fund Unit also have specific distribution polcies as they effect that class of
      unit. This class is for terms with wording of the form: " ... whether or not it is possible to hold shares ..." for
      a given parameter.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Policy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDistributionPolicy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund distribution policy
type: Ontology Class
---

# fund distribution policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDistributionPolicy>

## Definition

policy indicating the overall strategy or limitations on distribution for the fund

## Relationships

- **Subclass of**: [Policy](/concepts/fibo/FND/Law/LegalCapacity/Policy.md)

## Annotations

- **label** (en): fund distribution policy
- **definition** (en): policy indicating the overall strategy or limitations on distribution for the fund
- **explanatoryNote** (en): Note that individual classes of Fund Unit also have specific distribution polcies as they effect that class of unit. This class is for terms with wording of the form: " ... whether or not it is possible to hold shares ..." for a given parameter.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
