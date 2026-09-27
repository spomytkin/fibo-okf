---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real estate mortgage investment conduit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: special purpose vehicle that pools mortgage loans together and issues mortgage-backed securities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: REMIC
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A real estate mortgage investment conduit may be organized as a partnership, a trust, a corporation, or an association
      and is exempt from federal taxes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/owns
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.investopedia.com/terms/r/real-estate-mortgage-investment-conduit-remic.asp
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/RealEstateMortgageInvestmentConduit
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: real estate mortgage investment conduit
type: Ontology Class
---

# real estate mortgage investment conduit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/RealEstateMortgageInvestmentConduit>

## Definition

special purpose vehicle that pools mortgage loans together and issues mortgage-backed securities

## Relationships

- **See also**: [real-estate-mortgage-investment-conduit-remic.asp](<https://www.investopedia.com/terms/r/real-estate-mortgage-investment-conduit-remic.asp>)
- **Subclass of**: [SpecialPurposeVehicle](/concepts/fibo/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md)

## Constraints

- **[owns](/concepts/fibo/FND/OwnershipAndControl/Ownership/owns.md)**: min qualified cardinality 0 of type [MortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md)

## Annotations

- **label** (en): real estate mortgage investment conduit
- **definition** (en): special purpose vehicle that pools mortgage loans together and issues mortgage-backed securities
- **abbreviation** (en): REMIC
- **explanatoryNote** (en): A real estate mortgage investment conduit may be organized as a partnership, a trust, a corporation, or an association and is exempt from federal taxes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
