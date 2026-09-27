---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mandatory convertible bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convertible bond that converts into shares at maturity regardless of the equity price
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The conversion ratio at maturity reflects the equity price and par value of the bond when issued. There is also
      typically a second higher conversion ratio if the equity price rises above the strike during the term of the bond.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondConversionTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/ConvertibleBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MandatoryConvertibleBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: mandatory convertible bond
type: Ontology Class
---

# mandatory convertible bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MandatoryConvertibleBond>

## Definition

convertible bond that converts into shares at maturity regardless of the equity price

## Relationships

- **Subclass of**: [ConvertibleBond](/concepts/fibo/SEC/Debt/Bonds/ConvertibleBond.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [BondConversionTerms](/concepts/fibo/SEC/Debt/Bonds/BondConversionTerms.md)

## Annotations

- **label**: mandatory convertible bond
- **definition**: convertible bond that converts into shares at maturity regardless of the equity price
- **explanatoryNote**: The conversion ratio at maturity reflects the equity price and par value of the bond when issued. There is also typically a second higher conversion ratio if the equity price rises above the strike during the term of the bond.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
