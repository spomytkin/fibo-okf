---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exposure bearer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party subject to influence or risk arising from a specific contract, instrument, or arrangement
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Note that the name given to the party at risk is dependent on the jurisdiction and nature of the risk. Different
      regulations use differing terminology for this party, and exposure bearer is considered more general that some synonyms.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: exposed party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: risk bearer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: risk-bearing party
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedPartyIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Actor
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: exposure bearer
type: Ontology Class
---

# exposure bearer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer>

## Definition

party subject to influence or risk arising from a specific contract, instrument, or arrangement

## Relationships

- **Subclass of**: [Actor](<https://www.omg.org/spec/Commons/PartiesAndSituations/Actor>)

## Constraints

- **[isExposedPartyIn](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedPartyIn.md)**: some values from of type [ExposureSituation](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md)
- **[isExposedTo](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedTo.md)**: some values from of type [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)

## Annotations

- **label**: exposure bearer
- **definition**: party subject to influence or risk arising from a specific contract, instrument, or arrangement
- **note**: Note that the name given to the party at risk is dependent on the jurisdiction and nature of the risk. Different regulations use differing terminology for this party, and exposure bearer is considered more general that some synonyms.
- **synonym**: exposed party
- **synonym**: risk bearer
- **synonym**: risk-bearing party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
